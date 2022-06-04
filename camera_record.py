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
import icons
import cv2
import subprocess
from collections import deque
from pivideostream import PiVideoStream
from imutils.video import FPS
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import imutils

# initialize the camera and stream
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
stream = camera.capture_continuous(rawCapture, format="bgr",
	use_video_port=True)
# allow the camera to warmup and start the FPS counter
print("[INFO] sampling frames from `picamera` module...")
time.sleep(2.0)
fps = FPS().start()
# loop over some frames
for (i, f) in enumerate(stream):
	# grab the frame from the stream and resize it to have a maximum
	# width of 400 pixels
	frame = f.array
	frame = imutils.resize(frame, width=400)

	# clear the stream in preparation for the next frame and update
	# the FPS counter
	rawCapture.truncate(0)
	fps.update()
	# check to see if the desired number of frames have been reached
	if i == 20:
		break
# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# do a bit of cleanup
cv2.destroyAllWindows()
stream.close()
rawCapture.close()
camera.close()

def record_video():
	# created a *threaded *video stream, allow the camera sensor to warmup,
	# and start the FPS counter
	print("[INFO] sampling THREADED frames from `picamera` module...")
	vs = PiVideoStream().start()
	time.sleep(2.0)
	fps = FPS().start()

	timestr = time.strftime("%d%m%Y-%H%M%S")
	filename = 'video' + timestr + '.avi'
	video_writer = cv2.VideoWriter_fourcc('M','J','P','G')
	video_out = cv2.VideoWriter(filename, video_writer, 32.0, (320, 240))

	while True:
		frame1 = vs.read()
		video_out.write(frame1)
		fps.update()


