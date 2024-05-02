import logging
import sys
import os
from dataclasses import dataclass
from enum import Enum
from urllib.parse import quote_plus

import click
from datetime import datetime
from f1_23_telemetry.listener import TelemetryListener
from f1_23_telemetry.packets import *
from pymongo import MongoClient
from mongoengine import *

# Logging set-up
logger = logging.getLogger('shipper')
# logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)

connect('f1', host="mongo", username="root", password="example")


class Player(Enum):
    PRIMARY = 'primary'
    SECONDARY = 'secondary'


class CarTelemetryDataModel(Document):
    session_uid = StringField(required=True)
    session_time = StringField(required=True)
    player = EnumField(Player)  # primary or secondary
    speed = IntField()
    throttle = FloatField()
    brake = FloatField()
    drs = BooleanField()


class PackageMongoRepo:
    def __init__(self, host, user, password, db):
        uri = "mongodb://%s:%s@%s" % (
            quote_plus(user), quote_plus(password), host)
        self.client = MongoClient(uri)
        self.db = self.client[db]

    def write_telemetry(self, package: PacketCarTelemetryData):
        print(package.to_dict())
        print(f"Writing {package.to_dict()['car_telemetry_data'][package.header.player_car_index]}")
        self._write_player_telemetry(
            Player.PRIMARY,
            package_header=package.header,
            package=package.car_telemetry_data[
                package.header.player_car_index
            ]
        )
        if package.header.secondary_player_car_index != 255:
            print(f"Writing {package.to_dict()['car_telemetry_data'][package.header.secondary_player_car_index]}")
            self._write_player_telemetry(
                Player.SECONDARY,
                package_header=package.header,
                package=package.car_telemetry_data[
                    package.header.secondary_player_car_index
                ]
            )

    def _write_player_telemetry(self, player: Player, package_header: PacketHeader, package: CarTelemetryData):
        return CarTelemetryDataModel(
            session_uid=f"{package_header.session_uid}",
            session_time=f"{package_header.session_time}",
            player=player,
            speed=package.speed,
            throttle=package.throttle,
            brake=package.brake,
            drs=package.drs == 1
        ).save()


@click.command()
def ship():
    logger.info('Starting package shipping')
    listener = TelemetryListener(port=20777, host='0.0.0.0')
    package_repo = PackageMongoRepo(
        host="mongo",
        user="root",
        password="example",
        db="f1"
    )

    while True:
        try:
            package = listener.get()
            logger.info(f'Received packet of type {type(package)}')
            if isinstance(package, PacketCarTelemetryData):
                package_repo.write_telemetry(package)
        except KeyboardInterrupt:
            logger.info("Exiting")


if __name__ == '__main__':
    ship()
