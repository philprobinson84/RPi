#!/bin/sh
cd /home/pi/RPi/homekit
cp sample-camonly-config.json /home/pi/.homebridge/config.json

cd /tmp/
cd /home/pi/.homebridge/persist/
rm *.json
cd ..
rmdir persist/
cd ..

cd /home/pi/RPi/homekit
sudo cp sample-uv4l-raspicam.conf /etc/uv4l/uv4l-raspicam.conf
