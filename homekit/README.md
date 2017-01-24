#Quick Instructions

Setup blinkt, see below...

Now we'll copy the example JSON file over, change directory to wherever the blinkt examples reside, then:
```bash
cp homekit-sample-config.json /home/pi/.homebridge/config.json
```
To run everything, first we start the Python blinkt-homekit script:
```bash
sudo python homekit.py
```
Then start UV4L:
```bash
uv4l --auto-video_nr --driver raspicam --encoding mjpeg
```
Finally in another teminal just type:
```bash
homebridge
```

#Full Instructions

Based on the Using Mote with Homekit and Siri tutorial (https://learn.pimoroni.com/tutorial/sandyj/using-mote-with-homekit-and-siri) and modified to support Blinkt by Phil Robinson (https://github.com/philprobinson84/blinkt).

Borrow the easy setup of Flask and Mote from the aforementioned guide:
```bash
curl -sS get.pimoroni.com/mote | bash
```
Next, run:
```bash
sudo python homekit.py
```
Then, open another terminal window or tab, and type the following to test that our API is working as expected.
```bash
curl -i http://127.0.0.1:5000/blinkt/api/v1.0/on
```
That should have just turned your blinkt on! You should also be able to do this remotely, on another machine, replacing the 127.0.0.1 part of the URL with the IP address of the machine on which your API is running. You should also be able to do this in your web browser rather than with curl in the terminal.

Try typing the following to change the colour of the blinkt LEDs to red.
```bash
curl -i http://127.0.0.1:5000/blinkt/api/v1.0/set/FF0000
```
Set brightness (doesn't change the colour):
```bash
curl -i http://127.0.0.1:5000/blinkt/api/v1.0/brightness/50
```
N.B. Homebridge, and therefore our API, uses a brightness value of 0 to 100, which is translated by homekit.py to the range 0 to 1 required by the blinkt Python library.

Now for Homebridge installation and setup.

Open a terminal, and type the following to upgrade to the latest and greatest version of Node.js:
```bash
sudo apt-get update
sudo apt-get upgrade
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
```
Before we install homebridge, we'll also need to install a couple of dependencies. Type the following to install them:
```bash
sudo apt-get install libavahi-compat-libdnssd-dev
```
Now, we can install homebridge itself, as well as the homebridge-better-http-rgb and homebridge-camera-ffmpeg plugins:
```bash
sudo npm install -g --unsafe-perm homebridge
sudo npm install -g --unsafe-perm homebridge-better-http-rgb
sudo npm install -g --unsafe-perm homebridge-camera-ffmpeg
```
Now that everything is installed, we have to do a couple more things to configure homebridge correctly. homebridge is configured through a .json file that must be put into the /home/pi/.homebridge/ directory. We'll create that directory now:
```bash
mkdir /home/pi/.homebridge
```
Now we'll copy the example JSON file over, change directory to wherever the blinkt examples reside, then:
```bash
cp homekit-sample-config.json /home/pi/.homebridge/config.json
```
To run everything, first we start the Python script:
```bash
sudo python homekit.py
```
Then in another teminal just type:
```bash
homebridge
```
If you're running iOS 10 or above, you can now open the Home app and the device will be shown, allowing you to change colour, brightness and other goodness. Enjoy!

#Camera-Only Full Setup
##Installation
1. Download the latest Raspbian Jessie image and write to an SD card.
2. Boot your Pi (with camera connected).
3. If you're using WiFi, setup the WiFi now using the GUI.
4. Enable the camera, ssh and boot to cli, reboot when prompted.
5. Record a quick test video:
```bash
raspivid -o test.h264
```
6. Clone the Git repo, homekit branch:
```bash
git clone https://github.com/philprobinson84/RPi.git -b homekit
cd /home/pi/RPi/homekit
sudo chmod u+x *.sh
```
7. Install ffmpeg (taken from here: https://www.npmjs.com/package/homebridge-camera-ffmpeg-omx):
```bash
cd /home/pi/Downloads
sudo wget goo.gl/gMGA81 -O ffmpeg.deb
sudo dpkg -i ffmpeg.deb
```
8. Install the latest version of Node.JS (doesn't work on model B as it's ARMv6, use 'linux-armv6l' tarballs direct from nodejs.org, see 8 for ModelB.):
```bash
sudo apt-get update
sudo apt-get upgrade
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
```
8. Install the latest version of Node.JS (for model B):
```bash
cd /home/pi/Downloads
wget https://nodejs.org/dist/v6.9.4/node-v6.9.4-linux-armv6l.tar.xz
tar xf node-v6.9.4-linux-armv6l.tar.xz
cd node-v6.9.4-linux-armv6l
sudo cp -R * /usr/local/
```
Confirm the right version is now installed by running:
```bash
node -v
```
9. Install homebridge dependencies:
```bash
sudo apt-get install libavahi-compat-libdnssd-dev npm
```
10. Now, we can install homebridge itself, as well as the  homebridge-camera-ffmpeg-omx plugin:
```bash
sudo npm install -g --unsafe-perm homebridge
sudo npm install -g --unsafe-perm homebridge-camera-ffmpeg-omx
```
11. Now to install uv4l and a couple of extras for this:
(Based on this: http://www.linux-projects.org/uv4l/installation/)
Add repo key and repo to apt:
```bash
 curl http://www.linux-projects.org/listing/uv4l_repo/lrkey.asc | sudo apt-key add -
 sudo nano /etc/apt/sources.list
 ```
 Add the following line to the bottom of the file:
 ```
deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/ jessie main
 ```
 Hit `Ctrl+X` to exit - make sure to save changes!
 Now update apt and install UV4L:
 ```bash
 sudo apt-get update
 sudo apt-get install uv4l uv4l-raspicam
 ```
 Don't install uv4l-raspicam-extras unless you want the uv4l camera device to load automatically during boot (not recommended, better to enable when needed).

 ##Configuration
 Do the following any time you change the sample configuration files in this Git repo and wish to redeploy them.
 ```bash
 cd /home/pi/RPi/homekit
./cleanandcopy-camonly.sh
```
##Running
Finally, run the following script to launch UV4L and homebridge:
```bash
./run=camonly.sh
```
