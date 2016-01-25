#!/bin/bash

raspivid -w 1920 -h 1080 -b 15000000 -fps 30 -ISO 100 -ex auto -awb auto -mm average -a "RaspberryPi 1080p30 15Mbps ISO100" -t 60000 -vf -o spy_1080p30__15Mbps_ISO100_AutoEX.h264
raspivid -w 1920 -h 1080 -b 10000000 -fps 30 -ISO 100 -ex auto -awb auto -mm average -a "RaspberryPi 1080p30 10Mbps ISO100" -t 60000 -vf -o spy_1080p30__10Mbps_ISO100_AutoEX.h264
raspivid -w 1920 -h 1080 -b 5000000 -fps 30 -ISO 100 -ex auto -awb auto -mm average -a "RaspberryPi 1080p30 5Mbps ISO100" -t 60000 -vf -o spy_1080p30__5Mbps_ISO100_AutoEX.h264

raspivid -w 1920 -h 1080 -b 15000000 -fps 30 -ISO 400 -ex auto -awb auto -mm average -a "RaspberryPi 1080p30 15Mbps ISO400" -t 60000 -vf -o spy_1080p30__15Mbps_ISO400_AutoEX.h264
raspivid -w 1920 -h 1080 -b 10000000 -fps 30 -ISO 400 -ex auto -awb auto -mm average -a "RaspberryPi 1080p30 10Mbps ISO400" -t 60000 -vf -o spy_1080p30__10Mbps_ISO400_AutoEX.h264
raspivid -w 1920 -h 1080 -b 5000000 -fps 30 -ISO 400 -ex auto -awb auto -mm average -a "RaspberryPi 1080p30 5Mbps ISO400" -t 60000 -vf -o spy_1080p30__5Mbps_ISO400_AutoEX.h264

raspivid -w 1280 -h 720 -b 15000000 -fps 60 -ISO 100 -ex auto -awb auto -mm average -a "RaspberryPi 720p60 15Mbps ISO100" -t 60000 -vf -o spy_720p60__15Mbps_ISO100_AutoEX.h264
raspivid -w 1280 -h 720 -b 10000000 -fps 60 -ISO 100 -ex auto -awb auto -mm average -a "RaspberryPi 720p60 10Mbps ISO100" -t 60000 -vf -o spy_720p60__10Mbps_ISO100_AutoEX.h264
raspivid -w 1280 -h 720 -b 5000000 -fps 60 -ISO 100 -ex auto -awb auto -mm average -a "RaspberryPi 720p60 5Mbps ISO100" -t 60000 -vf -o spy_720p60__5Mbps_ISO100_AutoEX.h264

raspivid -w 1280 -h 720 -b 15000000 -fps 60 -ISO 400 -ex auto -awb auto -mm average -a "RaspberryPi 720p60 15Mbps ISO400" -t 60000 -vf -o spy_720p60__15Mbps_ISO400_AutoEX.h264
raspivid -w 1280 -h 720 -b 10000000 -fps 60 -ISO 400 -ex auto -awb auto -mm average -a "RaspberryPi 720p60 10Mbps ISO400" -t 60000 -vf -o spy_720p60__10Mbps_ISO400_AutoEX.h264
raspivid -w 1280 -h 720 -b 5000000 -fps 60 -ISO 400 -ex auto -awb auto -mm average -a "RaspberryPi 720p60 5Mbps ISO400" -t 60000 -vf -o spy_720p60__5Mbps_ISO400_AutoEX.h264