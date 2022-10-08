import pygame
import threading
import os
import time
import csv
import math
import sys, serial, board, busio, glob, argparse #, adafruit_lsm9ds1
import numpy as np
import datetime as dt
from datetime import datetime
from pygame.locals import *
import RPi.GPIO as GPIO
from time import sleep
#from bluetooth import *
import text
import icons
import cv2
import subprocess
from collections import deque
from pivideorecordandstream import PiVideoStreamRecord

#setup
#os.putenv('SDL_MOUSEDEV', '/dev/input/mouse')
#os.putenv('SDL_MOUSEDEV', '/dev/input/mouse0')
#os.putenv('SDL_FBDEV', '/dev/fb1')
#os.system ("sudo hciconfig hci0 piscan")
#os.environ["SDL_FBDEV"] = "/dev/fb1"

#Pygame setup
#pygame.mouse.set_visible(False)
pygame.init()
pygame.display.init()
pygame.mouse.set_visible(False)

#Pygame and font
screen = pygame.display.set_mode((240,320))
font = pygame.font.SysFont("comicsansms", 74)

#More OS stuff
#os.putenv('SDL_FBDEV', '/dev/fb1')
#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')

# Setup for physical buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

source = 0
#video_getter = VideoGet(source).start()
background = text.color_green

stream = cv2.VideoCapture(source)
# get the final frame size
width = 240
height = 320

menu = 0
controls = 0
cam = False
rec = False

menu_select = deque(['home', 'cam', 'nav', 'music', 'images'])
main_select = (70, 100)
cam_startup = True

while True:
	now = datetime.now()
	screen.fill(background)

	# Time text
	timestr = time.strftime("%d%m%Y-%H%M%S")
	clock = text.medFont.render(now.strftime("%I:%M:%S"), False, text.color_black)
	screen.blit(clock, (0,0))
	#print("Here")

	'''
	batt = subprocess.check_output('echo get battery | nc -q 0 127.0.0.1 8423', shell=True)
	batt = batt.decode("utf-8").split(": ")
	batt = int(float(batt[1].split("\n")[0]))
	batt_text = text.medFont.render("Batt: " + str(batt), False, text.color_black)
	screen.blit(batt_text, (0,0))
	'''

	up_image = pygame.transform.rotate(icons.left, 270)
	down_image = pygame.transform.rotate(icons.left, 90)
	if menu == 0:
		screen.blit(up_image, (70, 30))
		screen.blit(down_image, (70, 170))

		if menu_select[0] == 'home':
			screen.blit(icons.home, main_select)
		if menu_select[0] == 'cam':
			screen.blit(icons.vid, main_select)
		if menu_select[0] == 'nav':
			screen.blit(icons.nav, main_select)
		if menu_select[0] == 'music':
			screen.blit(icons.music, main_select)
		if menu_select[0] == 'images':
			screen.blit(icons.pics, main_select)

	if cam:
		# Displays live camera output on screen
		#frame = video_getter.frame
		#grabbed, frame1 = stream.read()

		if rec == True:
			print("RECORDING")

		if rec == False:
			print("NOT RECORDING")

		frame1 = vs.read()
		#frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
		#frame1 = cv2.flip(frame1, 1)
		#frame1 = pygame.surfarray.make_surface(frame1)
		#frame1 = pygame.transform.rotate(frame1, -90)
		frame1 = pygame.transform.scale(frame1, (220, 115))
		screen.blit(frame1, (10, 20))
		#screen.blit(frame1, (0,0), (10, 0, 230, 120))
		#pygame.display.update()


		if GPIO.input(6) == False:
			if rec == False:
				background = text.color_red
				vs.record()
				rec = True
			time.sleep(0.5)

		if GPIO.input(16) == False:
			if rec:
				background = text.color_yellow
				vs.stop_record()
				rec = False
			time.sleep(0.5)

		if GPIO.input(13) == False:
			#background = text.color_green
			#rec = False
			cam = False
			menu = 0
			time.sleep(0.5)



	#screen.blit(pygame.transform.flip(screen, True, False), (0, 0))
	pygame.display.update()

	if GPIO.input(16) == False:
		if menu == 0:
			menu_select.rotate(1)
		time.sleep(0.5)

	if GPIO.input(13) == False:
		if menu == 0:
			if menu_select[0] == 'cam':
				menu = 1
				if cam_startup == True:
					vs = PiVideoStreamRecord().start()
					cam_startup = False
				cam = True
				time.sleep(0.5)
		time.sleep(0.5)

	if GPIO.input(6) == False:
		if menu == 0:
			menu_select.rotate(-1)
		time.sleep(0.5)



