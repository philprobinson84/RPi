#!/bin/bash

# change to home dir
cd /home/pi

# install transmission
sudo apt-get -y install transmission-daemon

# stop transmission service
sudo service transmission-daemon stop

# copy over our config file
sudo cp /home/pi/RPi/tools/raspbmc/settings.json /etc/transmission-daemon/settings.json

# change the service config so it's run as root
sudo cp /home/pi/RPi/tools/raspbmc/transmission-daemon /etc/init.d/transmission-daemon

# restart the service
sudo service transmission-daemon start

# stop the firewall

sudo service iptables stop
# copy over iptables config allowing remote access
sudo cp /home/pi/RPi/tools/raspbmc/secure-rmc /etc/network/if-up.d/secure-rmc

# restart the firewall
sudo service iptables start
