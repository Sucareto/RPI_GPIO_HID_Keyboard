#!/usr/bin/python
import RPi.GPIO as GPIO
import signal
import time

KEY_LIST = (
    ( 7, "\x07"),  #D
    (11, "\x09"),  #F
    (13, "\x0a"),  #G
    (29, "\x0b"),  #H
    (31, "\x0d"),  #J
    (33, "\x0e"),  #K
    (15, "\x2c"),  #SPACE
)

keycode_tmp = "\x00" * 2


def signal_handler(signal, frame):
    f = open("/dev/hidg0", "w")
    f.write("\x00" * 8)
    f.close()
    GPIO.cleanup()
    exit()


signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BOARD)
for P in range(len(KEY_LIST)):
    GPIO.setup(KEY_LIST[P][0], GPIO.IN, pull_up_down=GPIO.PUD_UP)

while 1:

    ks = "\x00" * 2
    for K in range(len(KEY_LIST)):
        if GPIO.input(KEY_LIST[K][0]) is GPIO.LOW:
            ks += KEY_LIST[K][1]

    if keycode_tmp != ks:
        keycode_tmp = ks
        keycode = ks + "\x00" * (8 - len(ks))
        f = open("/dev/hidg0", "w")
        f.write(keycode[0:8])
        f.close()
    time.sleep(0.01)
