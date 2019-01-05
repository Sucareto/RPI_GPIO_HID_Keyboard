#!/usr/bin/python
import RPi.GPIO as GPIO
import signal

P_1 = 37
P_2 = 35
P_3 = 33
P_4 = 31

K_1 = '\x1D'	#Z
K_2 = '\x1B'	#X
K_3 = '\x06'	#C
K_4 = '\x19'	#V

def signal_handler(signal,frame):
	f = open('/dev/hidg0','w');
	f.write('\x00' * 8)
	f.close()
	GPIO.cleanup()
	exit()

signal.signal(signal.SIGINT,signal_handler)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(P_1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(P_2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(P_3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(P_4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
        f = open('/dev/hidg0','w');
	k1 = '\x00'
	k2 = '\x00'
	k3 = '\x00'
	k4 = '\x00'

        if GPIO.input(P_1) == GPIO.LOW:
		k1 = K_1

        if GPIO.input(P_2) == GPIO.LOW:
        	k2 = K_2

        if GPIO.input(P_3) == GPIO.LOW:
                k2 = K_3

	if GPIO.input(P_4) == GPIO.LOW:
                k2 = K_4

	keycode = '\x00' * 2 + k1 + k2 + k3 + k4 + '\x00' * 2
        f.write(keycode)
        f.close()
