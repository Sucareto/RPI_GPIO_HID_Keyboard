#!/usr/bin/python
import RPi.GPIO as GPIO
import signal
import time
import os

RUN = 40
KEY_LIST = {
	'V-L1':{'PIN':3,'KEY':'\x14'},#Q
	'V-L2':{'PIN':5,'KEY':'\x1a'},#W

	'V-R1':{'PIN':35,'KEY':'\x12'},#O
	'V-R2':{'PIN':37,'KEY':'\x13'},#P

	'BT-A':{'PIN':7,'KEY':'\x07'},#D
	'BT-B':{'PIN':11,'KEY':'\x09'},#F

	'BT-C':{'PIN':31,'KEY':'\x0d'},#J
	'BT-D':{'PIN':33,'KEY':'\x0e'},#K

	'FX-L':{'PIN':13,'KEY':'\x0a'},#G
	'FX-R':{'PIN':29,'KEY':'\x0b'},#H

	'START':{'PIN':15,'KEY':'\x28'},#ENTER
}

keycode_tmp = "\x00" * 2

def POW(PIN):
	GPIO.remove_event_detect(PIN)
	os.system('poweroff')
	clear(0,0)

def clear(signal,frame):
	f = open("/dev/hidg0","w");
	f.write("\x00" * 8)
	f.close()
	GPIO.cleanup()
	exit()

signal.signal(signal.SIGINT,clear)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
for P in KEY_LIST.keys():
	GPIO.setup(KEY_LIST[P]['PIN'],GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(RUN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(RUN,GPIO.FALLING,callback=POW,bouncetime=1000)

while 1:
	ks = "\x00" * 2
	for K in KEY_LIST.keys():
		if GPIO.input(KEY_LIST[K]['PIN']) is GPIO.LOW:
			ks += KEY_LIST[K]['KEY']

	if keycode_tmp != ks:
		keycode_tmp = ks
		keycode = ks + "\x00" * ( 8 - len(ks))
		f = open("/dev/hidg0","w");
	        f.write(keycode[0:8])
	        f.close()

	time.sleep(0.01)
