import time
import picamera
import os
from subprocess import call
from multiprocessing import Process
import glob
import shutil

VIDEO_DAYS = 1
FRAMES_PER_HOUR = 180
HOURS_IN_DAY = 24
FRAMES = FRAMES_PER_HOUR * HOURS_IN_DAY * VIDEO_DAYS
DIRNAME = "/home/pi/timelapse/"

UPLOAD_DROPBOX = 1
USE_SUBDIRS = 0
STITCH = 1
STITCH_ARCHIVE_SRC = 0
SECONDS_BETWEEN_STITCHES = 600
LAST_STITCH = time.time()


def stitch_init():
    print "stitch_init+"
    
    stitchDir = "/home/pi/timelapse/"
    
    # optionally mkdir and move source photos
    if STITCH_ARCHIVE_SRC == 1:
        TIME = time.localtime()
        CURRENT_YEAR = TIME[0]
        CURRENT_MONTH = TIME[1]
        CURRENT_DAY = TIME[2]
        CURRENT_HOUR = TIME[3]
        CURRENT_MIN = TIME[4]
        stitchDir = "/home/pi/timelapse/%04d%02d%02d_%02d%02d/" % (CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY, CURRENT_HOUR, CURRENT_MIN)
        if not os.path.isdir(stitchDir):
            os.makedirs(stitchDir)
            print "Created folder: %s" % stitchDir
        # move all jpgs
        src_dir = "/home/pi/timelapse/"
        dst_dir = stitchDir
        for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
            shutil.move(jpgfile, dst_dir)

    # spawn a process to run ffmpeg, then optionally upload to DropBox
    if __name__ == '__main__':
        p = Process(target=stitch_process, args=(stitchDir,))
        p.start()
        p.join()

def stitch_process(path):
    # run ffmpeg
    print "stitch_process+"
    inpath = path + "frame%03d.jpg"
    outpath = "/home/pi/%s_timelapse.mp4" % time.time()
    # FFMPEG CMD Line: ffmpeg -y -f image2 -i /home/phil/timelapse/frame%03d.jpg -start_number 0 -r 24 -vcodec libx264 -profile high /home/phil/timelapse.mp4
    call(['ffmpeg', '-y', '-f', 'image2', '-i', inpath, '-r', '24', '-vcodec', 'libx264', '-profile', 'high', outpath]) 
    
    # optionally upload to DropBox
    upload_init(outpath)

def upload_init(path):
    if UPLOAD_DROPBOX == 1:
        if __name__ == '__main__':
            p = Process(target=upload_process, args=(path,))
            p.start()
            p.join()        

def upload_process(path):
    uploadCmd = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload %s %s" % (path, path)
    call ([uploadCmd], shell=True)

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
        
        if USE_SUBDIRS == 1:
            create_dir()
        
        filename = '%sframe%03d.jpg' % (DIRNAME, frame)
        cam.capture(filename, format='jpeg',quality=75)
        
        upload_init(filename)

# Capture the images
for frame in range(FRAMES):
    # Note the time before the capture
    start = time.time()
    
    # capture one frame
    capture_frame(frame)
    
    # Wait for the next capture. Note that we take into
    # account the length of time it took to capture the
    # image when calculating the delay
    
    # periodically trigger a switch before sleeping
    if STITCH == 1:
        if time.time() > (LAST_STITCH + SECONDS_BETWEEN_STITCHES): 
    	    stitch_init()
	    LAST_STITCH = time.time()
    
    timeToSleep = int((60 * 60 / FRAMES_PER_HOUR) - (time.time() - start))
    if (timeToSleep < 1):
        print "timeToSleep was: %d! So set it to 1!" % timeToSleep
        timeToSleep = 1
    
    time.sleep(timeToSleep)
