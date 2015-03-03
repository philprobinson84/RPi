from __future__ import print_function 
import os 
for root, dirs, files in os.walk("/home/pi/timelapse"):
    for file in files:
        if file.endswith(".mp4"):
             print(os.path.join(root, file))
