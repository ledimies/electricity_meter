#!/usr/bin/python3
import pulser
import queue
import datetime
from influxdb import InfluxDBClient
from influxdb import SeriesHelper

# InfluxDB connections settings
influx_host = '192.168.1.2'
influx_port = 8086
influx_dbname = 'sahko'
influx_username = ''
influx_password = ''

myclient = InfluxDBClient(host=influx_host, port=influx_port, database=influx_dbname, username=influx_username, password=influx_password)
pulse_queue = queue.Queue()
pulsating_pulser = pulser.Pulser(pulse_queue)
previous_pulse = datetime.datetime.now()

class MySeriesHelper(SeriesHelper):
    """Instantiate SeriesHelper to write points to the backend."""

    class Meta:
        """Meta class stores time series helper configuration."""

        # The client should be an instance of InfluxDBClient.
        client = myclient

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'consumption'

        # Defines all the fields in this time series.
        fields = ['time', 'power']

        tags = []

        # Defines the number of data points to store prior to writing
        # on the wire.
        bulk_size = 1

        # autocommit must be set to True when using bulk_size
        autocommit = True


while True:
    try:
        pulse = pulse_queue.get(True, 1)
    except queue.Empty:
        print("Exception happened")
        continue
    diff = pulse - previous_pulse;
    elapsed_ms = (diff.days * 86400000) + (diff.seconds * 1000) + (diff.microseconds / 1000)
    power = 3600000 / elapsed_ms
    print("Pulse detected: {}ms {}W {}".format(elapsed_ms, power, int(pulse.timestamp() * 1000000000)))
    previous_pulse = pulse
    MySeriesHelper(time=pulse, power=power)
