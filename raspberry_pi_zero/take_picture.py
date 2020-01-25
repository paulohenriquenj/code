import picamera
from datetime import datetime
import time
from fractions import Fraction

picture_time = datetime.now().strftime('%Y%m%d_%H%M%S')

camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
time.sleep(5)
camera.capture(f'{picture_time}.jpg')
camera.stop_preview()