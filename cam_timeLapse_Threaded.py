#!/usr/bin/env python2.7
import time
from subprocess import call
from threading import Thread

cam_cmd = "python /home/pi/RPi/cam_timeLapse_Threaded_cam.py"
stitch_cmd = "python /home/pi/RPi/cam_timeLapse_Threaded_stitch.py"
upload_cmd = "python /home/pi/RPi/cam_timeLapse_Threaded_upload.py"

def cam_thread():
    print "cam_thread() - Starting Thread"
    start_time = time.time()
    call ([cam_cmd], shell=True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print "cam_thread() - Ended Thread (ran for: %.2f seconds)" % elapsed_time

def stitch_thread():
    print "stitch_thread() - Starting Thread"
    start_time = time.time()
    call ([stitch_cmd], shell=True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print "stitch_thread() - Ended Thread (ran for: %.2f seconds)" % elapsed_time

def upload_thread():
    print "upload_thread() - Starting Thread"
    start_time = time.time()
    call ([upload_cmd], shell=True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print "upload_thread() - Ended Thread (ran for: %.2f seconds)" % elapsed_time

# main
t_cam = Thread(target=cam_thread, args=())
t_cam.start()
#t_stitch = Thread(target=stitch_thread, args=())
#t_stitch.start()
#t_upload = Thread(target=upload_thread, args=())
#t_upload.start()
