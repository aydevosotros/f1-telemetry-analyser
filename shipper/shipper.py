import logging
import sys
import os
from urllib.parse import quote_plus

import click
from datetime import datetime
from f1_23_telemetry.listener import TelemetryListener
from f1_23_telemetry.packets import *
from pymongo import MongoClient

# Logging set-up
logger = logging.getLogger('shipper')
# logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)

INFLUX_TOKEN = os.getenv('INFLUX_TOKEN')


class PackageRepo:
    def __init__(self, host, user, password, db):
        uri = "mongodb://%s:%s@%s" % (
            quote_plus(user), quote_plus(password), host)
        self.client = MongoClient(uri)
        self.db = self.client[db]

    def write_package(self, package: PacketCarTelemetryData):
        player_index = package.header.player_car_index
        telemetry_collection = self.db.car_telemetry
        package_id = telemetry_collection.insert_one(package.to_dict())
        logger.info(f"Data saved with {package_id}")


@click.command()
def ship():
    logger.info('Starting package shipping')
    listener = TelemetryListener(port=20777, host='0.0.0.0')
    package_repo = PackageRepo(
        host="mongo:21017",
        user="root",
        password="example",
        db="f1"
    )

    while True:
        try:
            package = listener.get()
            logger.info(f'Received packet of type {type(package)}')
            if isinstance(package, PacketCarTelemetryData):
                package_repo.write_package(package)
        except KeyboardInterrupt:
            logger.info("Exiting")


if __name__ == '__main__':
    ship()
