#!/usr/bin/python
import RPi.GPIO as GPIO

PIN_A = 35
PIN_B = 37
key_z = '\x00\x00\x00\x1D\x00\x00\x00\x00'
key_x = '\x00\x00\x00\x1B\x00\x00\x00\x00'
key_zx= '\x00\x00\x1D\x1B\x00\x00\x00\x00'
close = '\x00\x00\x00\x00\x00\x00\x00\x00'

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_A,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_B,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
        f = open('/dev/hidg0','w');

        if GPIO.input(PIN_A) == GPIO.LOW and GPIO.input(PIN_B) == GPIO.LOW:
        	keycode = key_zx

        elif GPIO.input(PIN_A) == GPIO.LOW:
			keycode = key_z

        elif GPIO.input(PIN_B) == GPIO.LOW:
        	keycode = key_x

        else:
        	keycode = close

        f.write(keycode)
        f.close()

GPIO.cleanup()
