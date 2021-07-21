"""
F1-Telemetry-analyser shipper is an scripts that listens
to the UDP telemetry port from F1-2020 game and sends it
to an influx database
"""
import logging
import sys
import click

# Logging set-up
logger = logging.getLogger('shipper')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)


@click.command()
def ship():
    logger.info('Starting package shipping')


if __name__ == '__main__':
    ship()
