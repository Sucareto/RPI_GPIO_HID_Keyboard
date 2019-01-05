#!/usr/bin/python
import RPi.GPIO as GPIO
import signal

P_1 = 37
P_2 = 40
P_3 = 38
P_4 = 33

K_1 = "\x07"	#D
K_2 = "\x09"	#F
K_3 = "\x0d"	#J
K_4 = "\x0e"	#K

def signal_handler(signal,frame):
	f = open("/dev/hidg0","w");
	f.write("\x00" * 8)
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
        f = open("/dev/hidg0","w");
	k1 = ""
	k2 = ""
	k3 = ""
	k4 = ""

        if GPIO.input(P_1) == GPIO.LOW:
		k1 = K_1

        if GPIO.input(P_2) == GPIO.LOW:
        	k2 = K_2

        if GPIO.input(P_3) == GPIO.LOW:
                k3 = K_3

	if GPIO.input(P_4) == GPIO.LOW:
                k4 = K_4

	ks = "\x00" * 2 + k1 + k2 + k3 + k4
	keycode = ks + "\x00" * ( 8 - len(ks))
        f.write(keycode[0:8])
        f.close()
