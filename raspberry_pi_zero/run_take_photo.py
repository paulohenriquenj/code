import time
import subprocess
from datetime import datetime
import time


while True:
    picture_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    print('Taking photo!')
    cmd = f'raspistill -v -awb off -awbg 1.0,1.8 -w 1280 -h 960 -o /home/pi/imagens/{picture_time}.jpg'
    subprocess.call(cmd, shell=True)
    print('Sleeping')
    time.sleep(15)