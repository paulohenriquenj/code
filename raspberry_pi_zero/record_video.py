import picamera
import time 


cam = picamera.PiCamera()

cam.start_recording('/record_files/video.h264')

time.sleep(10)

cam.stop_recording()



