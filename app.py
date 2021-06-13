from flask import Flask, render_template, Response
import cv2, sys, time, os, imutils
import pantilthat as pth
from imutils.video import VideoStream


app = Flask(__name__)
vs = VideoStream(src=0).start()


@app.route('/')
def index():
    return render_template('index.html')


def vid_stream_imutlis():
    global vs
    while True:
        frame = vs.read()
        # frame = imutils.resize(frame, width=400)
        # encode to .JPG
        (flag, encodedImage) = cv2.imencode('.jpg', frame)
        if(not flag):
            continue
        yield (b'--frame\r\n' +
               b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) +
               b'\r\n')


def vid_stream():
    pth.pan(0)
    pth.tilt(-20)
    cap = cv2.VideoCapture(0)
    # FRAME_W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # FRAME_H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if(not ret):
            print('Error getting image.')
            continue
        # This line lets you mount the camera the "right" way up
        # with neopixels above
        # That is rotate 180 deg if the camera Ribbon is "on top"
        frame = cv2.flip(frame, 0)
        # encode to .JPG
        (flag, encodedImage) = cv2.imencode('.jpg', frame)
        if(not flag):
            continue
        yield (b'--frame\r\n' +
               b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) +
               b'\r\n')


@app.route('/vid_feed')
def vid_feed():
    return Response(
        # vid_stream_imutlis(),
        vid_stream(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
        )


if(__name__ == '__main__'):
    app.run(host='0.0.0.0',
            port=5000,
            debug=True,
            threaded=True,
            use_reloader=False)


#
# USE THESE COMMANDS TO RUN ON LOCAL NETWORK:
# export FLASK_APP=app
# sudo python3 app.py
#
# (this only runs locally: flask run)
#
# AND MAKE SURE IT IS IN RIGHT ENV
# source ~/.virtualenv/flask/bin/activate
