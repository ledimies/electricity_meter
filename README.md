# Electricity Meter

Electricity meter is an application for Raspberry Pi that can be used to measure electricity
consumption.

### Requirements

Raspberry Pi and Python 3 with influxdb library.

### Idea of operation

The main electricity cabinet has an electricity meter that has an LED light that pulses according
to the electricity use. 1000 impulses equals 1kWh. There is a simple phototransistor electric
circuit on top of the flashing led that generates a 5V pulse to a GPIO port of the Raspberry Pi.
The Python program measures time between each pulse and calculates the current power usage from
the time difference of the pulses. Each pulse with a timestamp and power consumption is stored
to an InfluxDB database.