import sys
import readchar
from sys import argv
import time
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(35, gpio.OUT)
gpio.setup(36, gpio.OUT)
gpio.setup(37, gpio.OUT)
gpio.setup(38, gpio.OUT)


try:
	while True:
			gpio.output(35, 1)
			gpio.output(36, 1)
			gpio.output(37, 1)
			gpio.output(38, 1)

	input = readchar.readkey();

	if input == '\x1b[D': 	#left
		gpio.output(35, 1)
		gpio.output(36, 0)
		gpio.output(37, 0)
		gpio.output(38, 1)
		time.sleep(1)

	if input == '\x1b[C':	#right
		gpio.output(35, 0)
		gpio.output(36, 1)
		gpio.output(37, 1)
		gpio.output(38, 0)
		time.sleep(1)

	if input == '\x1b[A':	#forward
		gpio.output(35, 1)
		gpio.output(36, 0)
		gpio.output(37, 1)
		gpio.output(38, 0)
		time.sleep(1)

	if input == '\x1b[B':	#backward
		gpio.output(35, 0)
		gpio.output(36, 1)
		gpio.output(37, 0)
		gpio.output(38, 1)
		time.sleep(1)

except KeyboardInterrupt:
	gpio.cleanup()
	sys.exit()