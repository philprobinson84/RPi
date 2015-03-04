#!/usr/bin/env python2.7
from __future__ import print_function 
from subprocess import call
import os 

def find_mp4s(path):
	# create text file for output
	mp4list = ''
	
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith(".mp4"):
				mp4list += os.path.join(root, file)
				mp4list += ' '
	
	return mp4list

def join_mp4s(mp4list, outpath):
	#call(['ffmpeg', '-f', 'concat', '-i', mp4list, '-c', 'copy', outpath])
	call(['mencoder', '-nosound', '-ovc', 'x264', '-lavfopts', 'format=mp4', '-idx', mp4list, '-o', outpath])
	

mp4list = find_mp4s("/home/pi/timelapse")
#print "mp4list is: %s " % mp4list
join_mp4s(mp4list,"/home/pi/timelapse/all.mp4")
