from picamera import PiCamera
import time
import numpy as np

camera = PiCamera()
time.sleep(2)
camera.resolution = (320, 240)
camera.vflip = True
camera.contrast = 10
file_name = "vid" + str(time.time()) + ".h264"
print("Start recording...")
camera.start_recording(file_name)
image = np.empty((240 * 320 * 3,), dtype=np.uint8)
camera.capture(image, 'bgr')
camera.wait_recording(5)
camera.stop_recording()
print("Done.")
