#!/bin/bash

#this script collects photos for stitching

# make directory called stitched-yyyymmdd-hhmmss

# move all .jpg files to new directory

# use ffmpeg to stitch mp4 from jpgs (consider switching to avconv?)




ffmpeg -y -f image2 -i /home/phil/timelapse/frame%03d.jpg -r 24 -vcodec libx264 -profile high /home/phil/timelapse.mp4



COUNTER=0
COUNTER2=0
while [ $COUNTER2 -lt 12 ]; do
 while [ $COUNTER -lt 120 ]; do
  let COUNTER=COUNTER+1
  DATE=$(date +"%Y-%m-%d_%H%M")
  raspistill -n -w 1920 -h 1080 -q 75 -o /home/pi/cam/$DATE.jpg
  cd /home/pi/Dropbox-Uploader
  ./dropbox_uploader.sh upload /home/pi/cam/$DATE.jpg $DATE.jpg
  sleep 60
 done
 cd /home/pi/cam
 ls *.jpg > stills.txt
 mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080 -o $DATE.avi -mf type=jpeg:fps=24 mf://@stills.txt
 rm *.txt
 cd /home/pi/Dropbox-Uploader
 ./dropbox_uploader.sh upload /home/pi/cam/$DATE.avi $DATE.avi
 cd /home/pi/cam
 rm *.jpg
 rm *.avi
done

