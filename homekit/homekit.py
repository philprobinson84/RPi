from colorsys import hsv_to_rgb, rgb_to_hsv
import blinkt
from flask import Flask, jsonify, make_response

app = Flask(__name__)

# Initialize blinkt device
blinkt.set_clear_on_exit(True)
blinkt.clear()
blinkt.show()

NUM_PIXELS = 8

# We're going to use a multi-dimensional (8x3) array / list to hold our status, colour and brightness for each of the 8 LEDs
status = []
for i in range(NUM_PIXELS):
    status.append(['FFFFFF', 0, 50])

colourAll = 'FFFFFF'

def hex_to_rgb(value):
    value = value.lstrip('#')
    length = len(value)
    return tuple(int(value[i:i + length / 3], 16) for i in range(0, length, length / 3))

def blinkt_on(p,c):
    global status
    r, g, b = hex_to_rgb(c)
    blinkt.set_pixel(p, r, g, b, float(status[p][2])/100)
    status[p][1] = 1
    status[p][0] = c
    blinkt.show()
    return True

def blinkt_off(p):
    global status
    blinkt.set_pixel(p, 0, 0, 0, float(status[p][2])/100)
    blinkt.show()
    status[p][1] = 0
    return True

def blinkt_brightness_get(p):
    global status
    return status[p][2]

def blinkt_brightness_set(p,b):
    global status
    status[p][2] = b
    blinkt_on(p,status[p][0])
    return True

def get_status(p):
    global status
    return status[p][1]

@app.route('/blinkt/api/v1.0/<int:p>/<string:st>', methods=['GET'])
def set_status(p,st):
    global status
    if st == 'on':
        blinkt_on(p,status[p][0])
    elif st == 'off':
        blinkt_off(p)
    elif st == 'status':
        ret = get_status(p)
    return str(get_status(p))

@app.route('/blinkt/api/v1.0/<int:p>/set', methods=['GET'])
def get_colour(p):
    global status
    return str(status[p][0])

@app.route('/blinkt/api/v1.0/<int:p>/set/<string:c>', methods=['GET'])
def set_colour(p,c):
    global status
    if status[p][1] != 0:
        blinkt_on(p,c)
    return str(c)

@app.route('/blinkt/api/v1.0/<int:p>/brightness', methods=['GET'])
def get_brightness(p):
    global status
    return str(status[p][2])

@app.route('/blinkt/api/v1.0/<int:p>/brightness/<string:x>', methods=['GET'])
def set_brightness(p,x):
    global status
    status[p][2] = int(x)
    if status[p][1] != 0:
        blinkt_on(p,status[p][0])
    return str(x)

@app.route('/blinkt/api/v1.0/<int:p>/all/<string:st>', methods=['GET'])
def set_status_all(p,st):
    global status
    ret = 0
    if st == 'on':
        for i in range(NUM_PIXELS):
            blinkt_on(i,status[i][0])
        ret = 1
    elif st == 'off':
        for i in range(NUM_PIXELS):
            blinkt_off(i)
        ret = 0
    elif st == 'status':
        # can't easily say whether all are off or on, so we'll take an average...
        totalOn = 0
        for i in range(NUM_PIXELS):
            totalOn += status[i][1]
        if totalOn<=3:
            ret = 0
        else:
            ret = 1
    return str(ret)

@app.route('/blinkt/api/v1.0/<int:p>/all/set', methods=['GET'])
def get_colour_all(p):
    global colourAll
    return str(colourAll)

@app.route('/blinkt/api/v1.0/<int:p>/all/set/<string:c>', methods=['GET'])
def set_colour_all(p,c):
    global colourAll
    colourAll = c
    for i in range(NUM_PIXELS):
        blinkt_on(i,colourAll)
    return str(c)

@app.route('/blinkt/api/v1.0/<int:p>/all/brightness', methods=['GET'])
def get_brightness_all(p):
    global status
    # can't easily get global brightness, so we'll take an average...
    totalBrightness = 0
    for i in range(NUM_PIXELS):
        totalBrightness += status[i][2]
    return str(round(totalBrightness/NUM_PIXELS,0))

@app.route('/blinkt/api/v1.0/<int:p>/all/brightness/<string:x>', methods=['GET'])
def set_brightness_all(p,x):
    global status
    for i in range(NUM_PIXELS):
        status[i][2] = int(x)
        if status[i][1] != 0:
            blinkt_on(i,status[i][0])
    return str(x)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    for i in range(NUM_PIXELS):
        blinkt_off(i)
    app.run(host='0.0.0.0', debug=True)
