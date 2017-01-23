#!/bin/sh
cd /home/pi/.homebridge/persist/
rm *.json
cd ..
rmdir persist/
cd ..

cd /home/pi/RPi/homekit
cp sample-config.json /home/pi/.homebridge/config.json

sudo cp sample-uv4l-raspicam.conf /etc/uv4l/uv4l-raspicam.conf
