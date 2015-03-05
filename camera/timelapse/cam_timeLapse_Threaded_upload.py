#!/usr/bin/env python2.7
import time
import os
from subprocess import call

import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

sys.stdout = Logger()

UPLOAD_INTERVAL = 60

def upload_file(inpath, outpath):
    uploadCmd = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload %s %s" % (inpath, outpath)
    call ([uploadCmd], shell=True)

while True:
	# record start_time
	start_time = time.time()
	
	# initiate the upload process
	inpath = "/home/pi/timelapse/latest/latest.jpg"
	outpath = "latest.jpg"
	if os.path.exists(inpath):
		upload_file(inpath,outpath)
		print "uploadThread: uploaded %s to %s" % (inpath,outpath)
	else:
		print "uploadThread: file %s does not exist, skipping" % (inpath)
	
	inpath = "/home/pi/timelapse/latest/latest.mp4"
	outpath = "latest.mp4"
	if os.path.exists(inpath):
		upload_file(inpath,outpath)
		print "uploadThread: uploaded %s to %s" % (inpath,outpath)
	else:
		print "uploadThread: file %s does not exist, skipping" % (inpath)
	
	# record end_time
	end_time = time.time()
	
	# determine elapsed time
	elapsed_time = end_time - start_time
	
	# determine how long to sleep
	sleep_time = UPLOAD_INTERVAL - elapsed_time
	
	# check for negative sleep request!
	if (sleep_time < 1):
		print "uploadThread: sleep_time < 1!!! (%s)" % sleep_time
		sleep_time = 1
	
	# sleep
	print "uploadThread: sleeping for %s seconds" % sleep_time
	time.sleep(sleep_time)
