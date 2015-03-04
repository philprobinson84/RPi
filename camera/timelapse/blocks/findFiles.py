from __future__ import print_function 
import os 

# create text file for output
f1=open('./mp4s.txt', 'w+')

for root, dirs, files in os.walk("/home/pi/timelapse"):
    for file in files:
        if file.endswith(".mp4"):
             print("file " + os.path.join(root, file), file=f1)
