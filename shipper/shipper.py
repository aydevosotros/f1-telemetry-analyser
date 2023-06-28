import logging
import sys
import click
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from f1_23_telemetry.listener import TelemetryListener

# Logging set-up
logger = logging.getLogger('shipper')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)


class PackageRepo:
    def __init__(self, influx_host, influx_port, influx_db, influx_token):
        self.influx_host = influx_host
        self.influx_port = influx_port
        self.influx_db = influx_db
        self.influx_token = influx_token

        self.influx_client = InfluxDBClient(
            url=f"http://{influx_host}:{influx_port}",
            token=influx_token,
            org="-")

        self.write_api = self.influx_client.write_api(
            write_options=SYNCHRONOUS
        )

    def write_package(self, package):
        json_body = [
            {
                "measurement": "f1_telemetry",
                "tags": {
                    "car_number": package['car_number']
                },
                "fields": package
            }
        ]
        self.write_api.write(self.influx_db, self.influx_org, json_body)


@click.command()
def ship():
    logger.info('Starting package shipping')
    listener = TelemetryListener(port=20777, host='localhost')
    package_repo = PackageRepo(
        influx_host='influxdb',
        influx_db='f1_telemetry',
        influx_port=8086,
        influx_token=None
    )
    while True:
        try:
            package = listener.get()
            logger.info(f'Received packet: {package}')
            package_repo.write_package(package)
        except KeyboardInterrupt:
            logger.info("Exiting")


if __name__ == '__main__':
    ship()
