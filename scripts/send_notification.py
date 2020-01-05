#!/usr/bin/env python
# -*- coding: utf-8
import sys
import subprocess


if len(sys.argv) == 3:
    sleep_time = int(sys.argv[1]) * 1 
    message = sys.argv[2]
    cmd = ' nohup sleep {}; notify-send "{}"'.format(str(sleep_time), message)

    subprocess.Popen(cmd, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

else:
    print('O primeiro parametro é minutos o segundo é a mensagem ')

