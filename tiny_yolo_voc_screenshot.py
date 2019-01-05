# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 23:05:45 2018

@author: USER
"""


import cv2
from darkflow.net.build import TFNet
import numpy as np
from grabscreen import grab_screen
import time
import threading

option = {
    #'model': 'cfg/yolo.cfg',
    'model': 'cfg/tiny-yolo-voc.cfg',
    #'load': 'bin/yolo.weights',
    'load': 'bin/tiny-yolo-voc.weights',
    'threshold': 0.15,
    'gpu': 0.4
}

tfnet = TFNet(option)

colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

label_name = None

def detection():
    stime = time.time()
    screen = cv2.resize(grab_screen(region=(0,0,1280,745)), (800,450))
    frame = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    results = tfnet.return_predict(frame)
    for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            global label_name
            label_name = label
            frame = cv2.rectangle(frame, tl, br, color, 7)
            frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow('screenshot',frame)
    print('FPS {:.1f}'.format(1 / (time.time() - stime)))

flag = True

def play_music(label_name):
    print('good')
    if label_name == 'car':
        print('find car, start play')
        time.sleep(5)
        print('car music end')
        
    if label_name == 'people':
        print('find people, start play')
        time.sleep(5)
        print('people music end')
        

class myThread (threading.Thread):
    def __init__(self, threadID, name, method, label_name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.method = str(method)
        self.label_name = label_name
    def run(self):
        print ("開始執行緒：" + self.name)
        if self.method == 'play_music':
            play_music(self.label_name)
        else :
            print("else")
        print ("退出執行緒：" + self.name)
        global flag

        flag = True



while True:
    detection()

    if flag:
        flag = False
        thread1 = myThread(1, "Thread-1", 'play_music', label_name)
        
        thread1.start()
        
    if cv2.waitKey(25) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          print('Detection ends.')
          break
    