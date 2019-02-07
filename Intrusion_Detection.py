import cv2
import numpy as np
from pushbullet import PushBullet
import pyttsx3
import time
import os
import json


camera_port = 0 
ramp_frames = 30 

#Your PushBullet API key
api_key ="o.IySlmUXS5Kam4p5WOrkOQpsJLYJ24spY"
pb =PushBullet(api_key)
pushMsg =pb.push_note("PYTHON : ","Found Internet Connectivity, is this you? if not message 'No' ")

def get_image(camera):
 retval, im = camera.read()
 return im 

#pushes captured image to Mobile
def Image_send():
    with open("Intruder.bmp", "rb") as pic:
        file_data = pb.upload_file(pic, "Intruder.bmp")

    push = pb.push_file(**file_data)

#log off PC if Intruder Suspected
def logOff():
    os.system("pmset displaysleepnow")


#Controller
def Control():
    count = 1
    while(count>0):
     time.sleep(20)
     val = pb.get_pushes()
     temp1 = [d['body'] for d in val]
     print(temp1)
     action = temp1[0]
     print(action)
     if(action == 'No'):
        
        camera = cv2.VideoCapture(camera_port)
        for i in range(ramp_frames):
            temp = camera.read()
        camera_capture = get_image(camera)
        cv2.imwrite("Intruder.bmp",camera_capture)
        del(camera)
        Image_send()
        count = count - 1
        time.sleep(5)
        logOff()
     else:
        break



Control()
