import time
import picamera
from subprocess import call

VIDEO_DAYS = 2
FRAMES_PER_HOUR = 120
FRAMES = FRAMES_PER_HOUR * 24 * VIDEO_DAYS

def capture_frame(frame):
    with picamera.PiCamera() as cam:
        time.sleep(2)
        cam.resolution = (1280, 720)
        dirname = time.strftime("%Y%m%d")
        cam.capture('/home/pi/timelapse/%s_frame%03d.jpg' % (dirname, frame),format='jpeg',quality=75)
        photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/timelapse/%s_frame%03d.jpg %s_frame%03d.jpg" % (dirname, frame, dirname, frame)
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
