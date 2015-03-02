#!/bin/bash

cd /home/pi

# https://github.com/atom/atom/blob/master/docs/build-instructions/linux.md

# Install some tools
sudo apt-get install build-essential git libgnome-keyring-dev fakeroot

# Build node.js (the version available via apt-get nodejs is too old, we need 0.10.x or 0.12.x)
# http://elinux.org/Node.js_on_RPi
wget http://nodejs.org/dist/v0.10.9/node-v0.10.9.tar.gz
tar -xzf node-v0.10.9.tar.gz
cd node-v0.10.9
./configure
make
sudo make install
cd ..

# check version of node and npm
node -v
npm -v

# ensure gyp uses Python2
npm config set python /usr/bin/python2 -g

# check node is set up ok
which node
# if above doesn't give a path, run the below cmd
sudo update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10

# build Atom
git clone https://github.com/atom/atom
cd atom
git fetch -p
git checkout $(git describe --tags `git rev-list --tags --max-count=1`)
script/build

# install Atom
sudo script/grunt install

# (optional) make a .deb package
script/grunt mkdeb

cd ..
