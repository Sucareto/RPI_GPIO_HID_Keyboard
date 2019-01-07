#!/usr/bin/python
import RPi.GPIO as GPIO
import signal
import time

P_1 = 33
P_2 = 35
P_3 = 37

P_4 = 36
P_5 = 38
P_6 = 40

K_1 = "\x07"	#D
K_2 = "\x09"	#F

K_3 = "\x0a"    #G
K_4 = "\x0b"    #H

K_5 = "\x0d"	#J
K_6 = "\x0e"	#K

keycode_tmp = ""

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
GPIO.setup(P_5,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(P_6,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while 1:
	k1,k2,k3,k4,k5,k6 = "","","","","",""

        if GPIO.input(P_1) is GPIO.LOW:
		k1 = K_1

        if GPIO.input(P_2) is GPIO.LOW:
        	k2 = K_2

        if GPIO.input(P_3) is GPIO.LOW:
                k3 = K_3

	if GPIO.input(P_4) is GPIO.LOW:
                k4 = K_4

        if GPIO.input(P_5) is GPIO.LOW:
                k5 = K_5

        if GPIO.input(P_6) is GPIO.LOW:
                k6 = K_6

	ks = "\x00" * 2 + k1 + k2 + k3 + k4 + k5 + k6

	if keycode_tmp != ks:
		keycode_tmp = ks
		keycode = ks + "\x00" * ( 8 - len(ks))
		f = open("/dev/hidg0","w");
	        f.write(keycode[0:8])
	        f.close()

	time.sleep(0.01)
