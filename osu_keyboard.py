#!/usr/bin/python
import RPi.GPIO as GPIO
import signal
import time

PIN_A = 37
PIN_B = 35

KEY_A = '\x1D'
KEY_B = '\x1B'

keycode_tmp = ""

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

while 1:
	k1,k2 = '\x00','\x00'

        if GPIO.input(PIN_A) is GPIO.LOW:
		k1 = KEY_A

        if GPIO.input(PIN_B) is GPIO.LOW:
        	k2 = KEY_B

	keycode = '\x00' * 2 + k1 + k2 + '\x00' * 4

	if keycode_tmp != keycode:
		keycode_tmp = keycode
		f = open("/dev/hidg0","w");
                f.write(keycode)
                f.close()

	time.sleep(0.01)
