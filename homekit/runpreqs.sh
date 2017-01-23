#!/bin/sh
uv4l --auto-video_nr --driver raspicam --encoding mjpeg --width 640 --height 360 --framerate 15
cd /home/pi/RPi/homekit
sudo python homekit.py
