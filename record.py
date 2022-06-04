from picamera import PiCamera
import time
camera = PiCamera()
time.sleep(2)
camera.resolution = (320, 240)
camera.vflip = True
camera.contrast = 10
file_name = "vid" + str(time.time()) + ".h264"
print("Start recording...")
camera.start_recording(file_name)
camera.wait_recording(5)
camera.stop_recording()
print("Done.")
