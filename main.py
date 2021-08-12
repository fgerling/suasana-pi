from prometheus_client import start_http_server, Summary, Gauge
import random
import time

import sys
import datetime

import Adafruit_DHT

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
TEMPERATURE = Summary('sensor_processing_seconds', 'Time spent processing sensor')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

@TEMPERATURE.time()
def process_sensor(temp, hum):
    sensor = Adafruit_DHT.AM2302
    pin = '4'
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity is not None and temperature is not None:
        temp.set(temperature)
        hum.set(humidity)
        print( '{:0.1f} - {:0.1f}'.format(temperature, humidity))

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    temp = Gauge("temperature", "Room temperature in celsius")
    hum = Gauge("humidity", "Room air humidity in percent")
    process_sensor(temp, hum)
    while True:
        time.sleep(30)
        process_sensor(temp, hum)

