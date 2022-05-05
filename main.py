import pygame
import threading
import os
import time
import csv
import math
import sys, serial, board, busio, glob, argparse, adafruit_lsm9ds1
import numpy as np
import datetime as dt
from datetime import datetime
from pygame.locals import *
import RPi.GPIO as GPIO
from time import sleep
from get_video import VideoGet
#from bluetooth import *
import text
import images
import cv2

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
screen = pygame.display.set_mode((240,135))
font = pygame.font.SysFont("comicsansms", 72)

#More OS stuff
#os.putenv('SDL_FBDEV', '/dev/fb1')
#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')

# Setup for physical buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

source = 0
#video_getter = VideoGet(source).start()
background = text.color_dark_green

stream = cv2.VideoCapture(source)
grabbed, frame = stream.read()

display = 0
controls = 0
cam = False

while True:
	now = datetime.now()
	screen.fill(background)

	# Time text
	clock = text.medFont.render(now.strftime("%I:%M:%S"), False, text.color_red)
	screen.blit(clock, (150,0))
	#print("Here")

	screen.blit(images.home, (25, 70))

	if cam:
		# Displays live camera output on screen
		#frame = video_getter.frame
		grabbed, frame1 = stream.read()
		#frame1 = frame.copy()
		frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
		frame1 = cv2.flip(frame1, 1)
		frame1 = pygame.surfarray.make_surface(frame1)
		#frame1 = pygame.transform.rotate(frame1, 90)
		frame1 = pygame.transform.scale(frame1, (220, 115))
		screen.blit(frame1, (10, 20))
		#screen.blit(frame1, (0,0), (10, 0, 230, 120))
		#pygame.display.update()

	screen.blit(pygame.transform.flip(screen, True, False), (0, 0))
	pygame.display.update()

	if GPIO.input(12) == False:
		background = text.color_green
		time.sleep(0.1)

	if GPIO.input(13) == False:
		background = text.color_orange
		time.sleep(0.1)

	if GPIO.input(16) == False:
		background = text.color_white
		time.sleep(0.1)

