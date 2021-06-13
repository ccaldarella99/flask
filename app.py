from flask import Flask, render_template, Response
# import cv2, sys, time, os
# from pantilthat import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# def vid_stream():
#     pan(0)
#     tilt(-20)
#     cap = cv2.VideoCapture(0)
#     FRAME_W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     FRAME_H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     while True:
#         if(not args.screen_capture):
#             # Capture frame-by-frame
#             ret, frame = cap.read()
#             # This line lets you mount the camera the "right" way up, with neopixels above
#             # Use this if the camera Ribbon is "on top"
#             frame = cv2.flip(frame, -1)
#             if ret == False:
#                 print("Error getting image")
#                 continue

# def vid_feed():
#     return Response(
#         vid_stream(), 
#         mimetype='multipart/x-mixed-replace; boundary=frame'
#         )

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)


#
# USE THESE COMMANDS TO RUN ON LOCAL NETWORK:
# export FLASK_APP=app
# sudo python3 app.py
#
# (this only runs locally: flask run)
#
# AND MAKE SURE IT IS IN RIGHT ENV
# source ~/.virtualenv/flask/bin/activate
