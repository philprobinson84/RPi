#!/usr/bin/env python2.7
import time
from subprocess import call

# Two test cases

# 1. stitch timelapse
def stitch_ffmpeg(path):
    # run ffmpeg
    print "stitchThread:stitch_process() starting stitch in: %s" % path
    inpath = path + "frame%06d.jpg"
    outpath = path + "timelapse.mp4"
    call(['ffmpeg', '-y', '-f', 'image2', '-i', inpath, '-r', '24', '-vcodec', 'libx264', '-profile', 'high', outpath])
    print "stitchThread:stitch_process() finished stitch in: %s" % path

# 2. transcode .mpeg2 to .h264

