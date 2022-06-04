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
		self.recording = False

	def start(self):
		# start the thread to read frames from the video stream
		self.cam_thread = Thread(target=self.update, args=())
		self.cam_thread.start()
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
		self.recording = True
		self.file_name = "video_" + str(time.time()) + ".h264"
		print("Start recording...")
		self.camera.start_recording(self.file_name)
	def stop_record(self):
		self.recording = False
		print("Stop recording...")
		self.camera.stop_recording()
	def stop(self):
		if self.recording == True:
			self.stop_recording()
			self.cam_thread.kill()
			self.camera.stop_preview()
			self.camera.close()
