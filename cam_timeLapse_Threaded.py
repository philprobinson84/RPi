#!/usr/bin/env python2.7
import time
from subprocess import call
from threading import Thread

cam_cmd = "python /home/pi/RPi/cam_timeLapse_Threaded_cam.py"
stitch_cmd = "python /home/pi/RPi/cam_timeLapse_Threaded_stitch.py"
upload_cmd = "python /home/pi/RPi/cam_timeLapse_Threaded_upload.py"

def cam_thread(i):
    print "cam_thread() - Starting Thread - Camera"
    start_time = time.time()
    call ([cam_cmd], shell=True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print "cam_thread() - Ended Thread - Camera (ran for: %.2f seconds)" % elapsed_time

# main
how_many = int(raw_input("How many threads?\n>"))

for i in range(how_many):
    t = Thread(target=process_thread, args=(i,))
    t.start()
