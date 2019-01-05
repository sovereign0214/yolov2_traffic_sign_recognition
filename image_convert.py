# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 01:11:34 2018

@author: USER
"""

import cv2
import os

#imdir = 'train_images/5101_Double_bend_right'
imdir = 'train_images/temp'

def flipped() :
    for img in os.scandir(imdir):
        
        image = cv2.imread(img.path) # remember to check if the ndarray of image is null
        
        flipped = cv2.flip(image, 1)
        cv2.imwrite(img.path, flipped)
        
    print("Done.")


def resize() :
    for img in os.scandir(imdir):
        
        image = cv2.imread(img.path) # remember to check if the ndarray of image is null
        
        resize = cv2.resize(image, (0, 0), 2, 2, cv2.INTER_CUBIC) # resize to twice larger than before
        cv2.imwrite(img.path, resize)

    print("Done.")


def test():    
    img = cv2.imread('doge.jpg')
    flipped = cv2.flip(img, 1)
    cv2.imshow('a', flipped)
    cv2.imwrite('doge_invert.jpg', flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#test()
#flipped()
resize()

# aware: the pic name can't be writed in Chinese
