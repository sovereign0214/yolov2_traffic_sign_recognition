# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 23:05:45 2018

@author: USER
"""


import cv2
from darkflow.net.build import TFNet
import numpy as np
from PIL import ImageGrab
import time
import threading
import pygame

option = {
    'model': 'cfg/tiny-yolo-voc-25c.cfg',
    'load': 45000,
    'threshold': 0.15,
    'gpu': 0.6
}

tfnet = TFNet(option)

colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

label_name = None

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
            global label_name
            label_name = label
            frame = cv2.rectangle(frame, tl, br, color, 7)
            frame = cv2.putText(frame, label+" "+str(confidence)+"%", tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow('screenshot',frame)
    print('FPS {:.1f}'.format(1 / (time.time() - stime)))

flag = True

def play_music(label_name):
    if label_name != None:
        if label_name[:11]=="Speed_limit":
            file='mp3/speed_limit.mp3' 
            pygame.mixer.init() 
            track = pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            time.sleep(1.35)
            pygame.mixer.music.stop()
        elif label_name[:13]=="Traffic_light":
            print("gg")
            file='mp3/traffic_light.mp3' 
            pygame.mixer.init() 
            track = pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            time.sleep(1.25)
            pygame.mixer.music.stop()
        elif label_name=="Bend_to_left":
            file='mp3/bend_to_left.mp3' 
            pygame.mixer.init() 
            track = pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            time.sleep(1.45)
            pygame.mixer.music.stop()
        elif label_name=="Bend_to_right":
            file='mp3/bend_to_right.mp3' 
            pygame.mixer.init() 
            track = pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            time.sleep(2)
            pygame.mixer.music.stop()
        elif label_name[:11]=="Double_bend":
            file='mp3/double_bend.mp3' 
            pygame.mixer.init() 
            track = pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            time.sleep(1.4)
            pygame.mixer.music.stop()
        elif label_name=="Fork_road":
            file='mp3/fork_road.mp3' 
            pygame.mixer.init() 
            track = pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            time.sleep(1.4)
            pygame.mixer.music.stop()
        elif label_name=="Narrow_road":
            file='mp3/narrow_road.mp3' 
            pygame.mixer.init() 
            track = pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            time.sleep(1.45)
            pygame.mixer.music.stop()
        elif label_name=="No_entry":
            file='mp3/no_entry.mp3' 
            pygame.mixer.init() 
            track = pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            time.sleep(1.4)
            pygame.mixer.music.stop()
        elif label_name=="No_left_turn":
            file='mp3/no_left_turn.mp3' 
            pygame.mixer.init() 
            track = pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            time.sleep(1.55)
            pygame.mixer.music.stop()
        elif label_name=="No_right_turn":
            file='mp3/no_right_turn.mp3' 
            pygame.mixer.init() 
            track = pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            time.sleep(1.5)
            pygame.mixer.music.stop()
        elif label_name=="No_u_turn":
            file='mp3/no_u_turn.mp3' 
            pygame.mixer.init() 
            track = pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            time.sleep(1.5)
            pygame.mixer.music.stop()
    else:
        print(label_name)
        

class myThread (threading.Thread):
    def __init__(self, threadID, name, method, label_name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.method = str(method)
        self.label_name = label_name
    def run(self):
        print ("Start thread ：" + self.name)
        if self.method == 'play_music':
            play_music(self.label_name)
        else :
            print("else")
        print ("Exit thread ：" + self.name)
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
    