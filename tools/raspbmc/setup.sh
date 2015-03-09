#!/bin/bash

# change to home dir
cd /home/pi

# install transmission
sudo apt-get -y install transmission-daemon

# stop transmission service
sudo service transmission-daemon stop

# copy over our config file
