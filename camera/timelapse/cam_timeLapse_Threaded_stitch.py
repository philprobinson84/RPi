#!/usr/bin/env python2.7
import time
import os
import errno
from subprocess import call

STITCH_INTERVAL = 3600

def force_symlink(file1, file2):
    try:
        os.symlink(file1, file2)
    except OSError, e:
        if e.errno == errno.EEXIST:
            os.remove(file2)
            os.symlink(file1, file2)
            

def stitch_process(path):
    # run ffmpeg
    print "stitchThread:stitch_process() starting stitch in: %s" % path
    inpath = path + "frame%06d.jpg"
    outpath = path + "timelapse.mp4"
    # FFMPEG CMD Line: ffmpeg -y -f image2 -i /home/phil/timelapse/frame%03d.jpg -start_number 0 -r 24 -vcodec libx264 -profile high /home/phil/timelapse.mp4
    call(['ffmpeg', '-y', '-f', 'image2', '-i', inpath, '-r', '24', '-vcodec', 'libx264', '-profile', 'high', outpath])
    print "stitchThread:stitch_process() finished stitch in: %s" % path
    force_symlink(outpath, "/home/pi/timelapse/latest/latest.mp4")

# first off, we need to wait until the hour before we can start our loop
while True:
    TIME = time.localtime()
    CURRENT_YEAR = TIME[0]
    CURRENT_MONTH = TIME[1]
    CURRENT_DAY = TIME[2]
    CURRENT_HOUR = TIME[3]
    CURRENT_MINS = TIME[4]
    print "stitchThread: finding first hour, current minutes: %d" % CURRENT_MINS

    if (CURRENT_MINS == 5):
        print "stitchThread: it's now 5 minutes past an hour, moving onto main loop"
        break

    print "stitchThread: sleeping for 30s..."
    time.sleep(30)

while True:
    # record start_time
    start_time = time.time()

    # work out the path to use
    TIME = time.localtime()
    CURRENT_YEAR = TIME[0]
    CURRENT_MONTH = TIME[1]
    CURRENT_DAY = TIME[2]
    CURRENT_HOUR = TIME[3]
    DIRNAME = "/home/pi/timelapse/%04d%02d%02d_%02d/" % (CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, (CURRENT_HOUR-1))

    # initiate the stitch process
    stitch_process(DIRNAME)

    # record end_time
    end_time = time.time()

    # determine elapsed time
    elapsed_time = end_time - start_time

    # determine how long to sleep
    sleep_time = STITCH_INTERVAL - elapsed_time

    # check for negative sleep request!
    if (sleep_time < 1):
        print "stitchThread: sleep_time < 1!!! (%s)" % sleep_time
        sleep_time = 1

    # sleep
    print "stitchThread: sleeping for %s seconds" % sleep_time
    time.sleep(sleep_time)
