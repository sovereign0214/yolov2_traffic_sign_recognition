# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 23:05:45 2018

@author: USER
"""


import cv2
from darkflow.net.build import TFNet
import numpy as np
#this import is for TX2
import pyscreenshot as ImageGrab
import time

option = {
    'model': 'cfg/tiny-yolo-voc-25c.cfg',
    'load': 76500,
    'threshold': 0.15,
    'gpu': 0.5
}

tfnet = TFNet(option)

colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

def detection():
    stime = time.time()
    screen = np.array(ImageGrab.grab(bbox=(0,140,1000,1040)))
    frame = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    results = tfnet.return_predict(frame)
    for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence=("%.2f"%(result['confidence']*100))
            frame = cv2.rectangle(frame, tl, br, color, 7)
            frame = cv2.putText(frame, label+" "+str(confidence)+"%", tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow('screenshot',frame)
    print('FPS {:.1f}'.format(1 / (time.time() - stime)))


while True:
    detection()
        
    if cv2.waitKey(25) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          print('Detection ends.')
          break
    