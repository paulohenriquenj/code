import picamera
import time 
import subprocess
import os


cam = picamera.PiCamera()

record_dir = 'record_files'

file_h264 = record_dir + '/video.h264'

file_mp4 = record_dir + '/video.mp4'

cam.start_recording(file_h264)

time.sleep(10)

cam.stop_recording()

if os.path.isfile(file_h264) :
    cmd = f'ffmpeg -y -framerate 24 -i {file_h264} -c copy {file_mp4}'
    subprocess.call(cmd, shell=True)



