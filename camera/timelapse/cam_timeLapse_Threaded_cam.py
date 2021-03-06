#!/usr/bin/env python2.7
import time
import picamera
import os
import errno

import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

sys.stdout = Logger()

FRAME_INTERVAL = 30
DIRNAME = "/home/pi/timelapse"
frame = 1

def create_dir():
    TIME = time.localtime()
    CURRENT_YEAR = TIME[0]
    CURRENT_MONTH = TIME[1]
    CURRENT_DAY = TIME[2]
    CURRENT_HOUR = TIME[3]

    global DIRNAME
    DIRNAME = "/home/pi/timelapse/%04d%02d%02d_%02d/" % (CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, CURRENT_HOUR)
    #print "DIRNAME = %s" % DIRNAME
    if not os.path.isdir(DIRNAME):
        os.makedirs(DIRNAME)
        print "camThread:create_dir() created folder: %s" % DIRNAME
        global frame
        frame = 1
        print "camThread:create_dir() frame # reset to: %d" % frame

def force_symlink(file1, file2):
    try:
        os.symlink(file1, file2)
    except OSError, e:
        if e.errno == errno.EEXIST:
            os.remove(file2)
            os.symlink(file1, file2)


def capture_frame(frame):
    with picamera.PiCamera() as cam:
        time.sleep(1)

        cam.resolution = (1280, 720)

        create_dir()
        global DIRNAME
        filename = '%sframe%06d.jpg' % (DIRNAME, frame)
        cam.capture(filename, format='jpeg',quality=75)
        print "camThread:capture_frame() captured frame %06d: %s" % (frame, filename)
        force_symlink(filename, "/home/pi/timelapse/latest/latest.jpg")


while True:
    # record start_time
    start_time = time.time()

    # capture a frame
    capture_frame(frame)

    # increment frame#
    frame += 1

    # record end time
    end_time = time.time()

    # determine elapsed time
    elapsed_time = end_time - start_time

    # determine how long to sleep
    sleep_time = FRAME_INTERVAL - elapsed_time

    # check for negative sleep request!
    if (sleep_time < 1):
        print "camThread: sleep_time < 1!!! (%s)" % sleep_time
        sleep_time = 1

    # sleep
    print "camThread: sleeping for %s seconds" % sleep_time
    time.sleep(sleep_time)
