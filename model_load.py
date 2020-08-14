# importing libraries 

import numpy as np 
import cv2 
import tensorflow as tf
import os
import urllib.request
import time
from multiprocessing import Process
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from twilio.rest import Client


#function to make predictions using saved model
def predict_now(img,model):


    resize = cv2.resize(img,(160,160))
    rgb = cv2.cvtColor(resize,cv2.COLOR_BGR2RGB)
    test2 = rgb[np.newaxis is None,:,:,:]

    #make prediction and calculate time required
    start = time.time()
    predictions = model.predict(test2)
    end = time.time()
    os.system('clear')

    print('Predictions:{} Time taken: {}\n'.format(predictions[0][0], end-start))
    
    #based of model predictions send out message to user on whatasapp if there is a fire hazaard detected 
    if predictions < -1 :
        print('Fire hazard!\n')
        
        client.messages.create(body='Fire Hazard',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

    elif predictions > -1 and predictions < 1.5:
        print('Warning posibility of fire\n')
        
        client.messages.create(body='warning Possible Fire Hazard',
               from_=from_whatsapp_number,
               to=to_whatsapp_number)

    else:
        print('No fire hazard\n')

    time.sleep(1)
    print('New image capture')

    return predictions[0][0], end-start



#stream from a link or use webcams connected to the device
source = 'rtsp://192.168.0.102:8080/video/h264'

    #OR 

# source = 0

#path to model on the device
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path_to_model = os.path.join(BASE_DIR, 'fire_detect_model')
client = Client()

#using twilo to detect number
from_whatsapp_number='whatsapp:+14155238886'

to_whatsapp_number='whatsapp:+918286838255'

#loac model
model = tf.keras.models.load_model(path_to_model)

if __name__ == '__main__':


    cap = cv2.VideoCapture(source)
    start = start = time.time()
    diff=1
    while(1): 
        # make predictions every 6 seconds 
        if int(diff)%6 == 0:
            predict_now(img,model)

        ret, img = cap.read();

        cv2.imshow('image', img)

        #calc time elasped
        end = time.time()
        diff = end-start

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()