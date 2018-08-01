import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

go1 = 17
GPIO.setup(go1,GPIO.OUT)
servo = GPIO.PWM(go1,50)


