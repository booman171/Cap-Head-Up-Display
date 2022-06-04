# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from threading import Thread
import cv2
import time
import io
import pygame

class PiVideoStreamRecord:
	def __init__(self, resolution=(320, 240), framerate=32):
		# initialize the camera and stream
		self.camera = PiCamera()
		self.camera.resolution = resolution
		self.rgb = bytearray(self.camera.resolution[0] * self.camera.resolution[1] * 3)
		#self.camera.framerate = framerate
		#self.rawCapture = PiRGBArray(self.camera, size=resolution)
		#self.stream = self.camera.capture_continuous(self.rawCapture,
		#	format="bgr", use_video_port=True)
		# initialize the frame and the variable used to indicate
		# if the thread should be stopped
		#self.frame = None
		#self.stopped = False
		#Specify width and height of video to be recorded
		#self.vid_w = 320
		#self.vid_h = 240
		#Intiate codec for Video recording object
		#self.fourcc = cv2.VideoWriter_fourcc(*'DIVX')
		#self.timestr = time.strftime("%d%m%Y-%H%M%S")
		#self.filename = 'video' + self.timestr + '.avi' # .avi .mp4
		#self.fps = 15.0
		#self.video_writer = cv2.VideoWriter_fourcc('M','J','P','G')
		#self.video_out = cv2.VideoWriter(self.filename, self.video_writer, 15.0, (320, 240))

	def start(self):
		# start the thread to read frames from the video stream
		Thread(target=self.update, args=()).start()
		print("uyt")
		return self
	def update(self):
		while(True):
			self.stream = io.BytesIO()

			self.camera.capture(self.stream, use_video_port=True, format='rgb')
			self.stream.seek(0)
			self.stream.readinto(self.rgb)
			self.stream.close()
			self.frame = pygame.image.frombuffer(self.rgb[0:
	  			(self.camera.resolution[0] * self.camera.resolution[1] * 3)],
	  			 self.camera.resolution, 'RGB')

	def read(self):
		# return the frame most recently read
		return self.frame
	def record(self):
		self.file_name = "viddddddd" + str(time.time()) + ".h264"
		print("Start recording...")
		self.camera.start_recording(self.file_name)
	def stop_record(self):
		print("Stop recording...")
		self.camera.stop_recording()
	def stop(self):
		# indicate that the thread should be stopped
		self.stopped = True
