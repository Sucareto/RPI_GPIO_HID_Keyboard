#!/usr/bin/python
import RPi.GPIO as GPIO
import signal
import time

KEY1 = [37,'\x1D']
KEY2 = [35,'\x1B']

keycode_tmp = '\x00' * 8

def signal_handler(signal,frame):
	f = open('/dev/hidg0','w')
	f.write('\x00' * 8)
	f.close()
	GPIO.cleanup()
	exit()

signal.signal(signal.SIGINT,signal_handler)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(KEY1[0],GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY2[0],GPIO.IN,pull_up_down=GPIO.PUD_UP)

while 1:
        k1 = KEY1[1] if GPIO.input(KEY1[0]) is GPIO.LOW else "\x00"

        k2 = KEY2[1] if GPIO.input(KEY2[0]) is GPIO.LOW else "\x00"

	keycode = '\x00' * 2 + k1 + k2 + '\x00' * 4

	if keycode_tmp != keycode:
		keycode_tmp = keycode
		f = open("/dev/hidg0","w")
                f.write(keycode)
                f.close()

	time.sleep(0.01)
