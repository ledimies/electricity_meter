import datetime
import RPi.GPIO as GPIO

class Pulser(object):
    def __init__(self, jono):
        self.jono = jono
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(8, GPIO.FALLING, callback=self.__onPulse, bouncetime=60)

    def __onPulse(self, channel):
        self.jono.put(datetime.datetime.now())


