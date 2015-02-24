import time
import picamera
import os
from subprocess import call

VIDEO_DAYS = 1
FRAMES_PER_HOUR = 120
HOURS_IN_DAY = 24
FRAMES = FRAMES_PER_HOUR * HOURS_IN_DAY * VIDEO_DAYS
DIRNAME = "/home/pi/timelapse"

def create_dir():
    TIME = time.localtime()
    CURRENT_YEAR = TIME[0]
    CURRENT_MONTH = TIME[1]
    CURRENT_DAY = TIME[2]
    CURRENT_HOUR = TIME[3]

    print "CURRENT_YEAR = %d" % TIME[0]
    print "CURRENT_MONTH = %d" % TIME[1]
    print "CURRENT_DAY = %d" % TIME[2]
    print "CURRENT_HOUR = %d" % TIME[3]

    global DIRNAME
    DIRNAME = "/home/pi/timelapse/%s%s%s_%s/" % (CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, CURRENT_HOUR)
    print "DIRNAME = %s" % DIRNAME
    if not os.path.isdir(DIRNAME):
        os.makedirs(DIRNAME)
        print "Created folder: %s" % DIRNAME 

def capture_frame(frame):
    with picamera.PiCamera() as cam:
        #time.sleep(2)
        cam.resolution = (1280, 720)
        create_dir()
        cam.capture('%sframe%03d.jpg' % (DIRNAME, frame),format='jpeg',quality=75)
        photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload %sframe%03d.jpg %sframe%03d.jpg" % (DIRNAME, frame, DIRNAME, frame)
        call ([photofile], shell=True)
        photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload %sframe%03d.jpg latest.jpg" % (DIRNAME, frame)
        call ([photofile], shell=True)

# Capture the images
for frame in range(FRAMES):
    # Note the time before the capture
    start = time.time()
    capture_frame(frame)
    # Wait for the next capture. Note that we take into
    # account the length of time it took to capture the
    # image when calculating the delay
    time.sleep(
        int(60 * 60 / FRAMES_PER_HOUR) - (time.time() - start)
    )
