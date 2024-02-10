#pip install OPi.GPIO
import OPi.GPIO as GPIO
import time
pin = 14
GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)
try:
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
finally:
    GPIO.cleanup()