import logging
import sys
import os
import click
from datetime import datetime
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from f1_23_telemetry.listener import TelemetryListener
from f1_23_telemetry.packets import *

# Logging set-up
logger = logging.getLogger('shipper')
# logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)

INFLUX_TOKEN = os.getenv('INFLUX_TOKEN')


class PackageRepo:
    def __init__(self, influx_host, influx_port, influx_db, influx_token):
        self.influx_host = influx_host
        self.influx_port = influx_port
        self.influx_db = influx_db
        self.influx_token = influx_token

        self.influx_client = InfluxDBClient(
            url=f"http://{influx_host}:{influx_port}", token=influx_token)

        self.write_api = self.influx_client.write_api(
            write_options=SYNCHRONOUS
        )

    def write_package(self, package: PacketCarTelemetryData):
        player_index = package.header.player_car_index
        point = Point("CarTelemetry")
        point.time(datetime.now())
        [point.field(k, v) for k, v in package.car_telemetry_data[player_index].to_dict().items() if not isinstance(v, list)]
        self.write_api.write(bucket='telemetry', org='my-org', record=[point])
        logger.info("Data sent to influx")


@click.command()
def ship():
    logger.info('Starting package shipping')
    listener = TelemetryListener(port=20777, host='0.0.0.0')
    package_repo = PackageRepo(
        influx_host='influxdb',
        influx_db='f1_telemetry',
        influx_port=8086,
        influx_token=INFLUX_TOKEN,
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
