# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:21:23 2018

@author: USER
"""

import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

option = {
    #'model': 'cfg/yolo.cfg',
    'model': 'cfg/tiny-yolo-voc.cfg',
    #'load': 'bin/yolo.weights',
    'load': 'bin/tiny-yolo-voc.weights',
    'threshold': 0.15,
    'gpu': 0.6
}

tfnet = TFNet(option)

capture = cv2.VideoCapture('videoplayback.mp4')
colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

while (capture.isOpened()):
    stime = time.time()
    ret, frame = capture.read()
    results = tfnet.return_predict(frame)
    if ret:
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            frame = cv2.rectangle(frame, tl, br, color, 7)
            frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            print('Detection ends.')
            break
    else:
        capture.release()
        cv2.destroyAllWindows()
        break