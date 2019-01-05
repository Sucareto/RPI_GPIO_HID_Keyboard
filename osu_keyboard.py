#!/usr/bin/python
import RPi.GPIO as GPIO
import signal

PIN_A = 37
PIN_B = 35

KEY_A = '\x1D'
KEY_B = '\x1B'

def signal_handler(signal,frame):
	f = open('/dev/hidg0','w');
	f.write('\x00' * 8)
	f.close()
	GPIO.cleanup()
	exit()

signal.signal(signal.SIGINT,signal_handler)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_A,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_B,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
        f = open('/dev/hidg0','w');

	k1 = '\x00'
	k2 = '\x00'

        if GPIO.input(PIN_A) == GPIO.LOW:
		k1 = KEY_A

        if GPIO.input(PIN_B) == GPIO.LOW:
        	k2 = KEY_B

	keycode = '\x00' * 2 + k1 + k2 + '\x00' * 4
        f.write(keycode)
        f.close()
