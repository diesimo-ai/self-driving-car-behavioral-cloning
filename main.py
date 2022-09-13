# File : main.py 
# Description : launch the main application 
#
# Libraries requirements : 
#   <os> : standard library
#		- Provides a portable way of using operating system dependent functionality.
#   <sys> : standard library
#		- provides access to some variables used or maintained by the interpreter and 
#         to functions that interact strongly with the interpreter.
#   <json> : standard library
#		- Provides functionalites for data storing and serialization
#   <numpy> : standard library
#		- Provides multidimensional arrays and linear algebra tools, optimized for speed
#
# File history :
# Afondiel  |  14.03.2021 | Creation 
# Afondiel  |  13.09.2022 | Last modification
#  
import os
import sys
import socketio
import eventlet
import numpy as np
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import cv2
# from src import drive

# real time communication between client and server 
sio = socketio.Server()
 
app = Flask(__name__) #'__main__'
speed_limit = 10
def img_preprocess(img):
    img = img[60:135,:,:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img,  (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img/255
    return img
 
 
@sio.on('telemetry')
def telemetry(sid, data):
    speed = float(data['speed'])
    image = Image.open(BytesIO(base64.b64decode(data['image'])))
    image = np.asarray(image)
    image = img_preprocess(image)
    image = np.array([image])
    steering_angle = float(model.predict(image))
    # forcing speed limit
    throttle = 1.0 - speed/speed_limit
    print('{} {} {}'.format(steering_angle, throttle, speed))
    send_control(steering_angle, 1.0)
 
 
# connect, disconnect, message event
# as soon as the connect is stablished we send the control command for streering angle and throttle
@sio.on('connect')
def connect(sid, my_env):
    print('Connected')
    send_control(0, 0)
 
def send_control(steering_angle, throttle):
    sio.emit('steer', data = {
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    })
 
 
if __name__ == '__main__':
    # load the model
    # model = load_model('model.h5')
    model = load_model('.\data\models\model_gen.h5')
    # combine sio and flask
    # middleware to dispatch the data between sio and app
    app = socketio.Middleware(sio, app)
    # create a socket
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)

    # @TODO : Retraining the model with more epochs
    # Retraining the model with more datas
   