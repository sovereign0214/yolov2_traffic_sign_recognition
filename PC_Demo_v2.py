import cv2
from darkflow.net.build import TFNet
import numpy as np
from PIL import ImageGrab
import time
import threading
import pygame
import math

option = {
    'model': 'cfg/tiny-yolo-voc-25c.cfg',
    'load': 45000,
    'threshold': 0.15,
    'gpu': 0.6
}

tfnet = TFNet(option)

colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

list_same_sign = []
label_name = None 
same_sign = False

def detection():
    stime = time.time()
    screen = np.array(ImageGrab.grab(bbox=(0,140,800,740)))
    frame = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    font = cv2.FONT_HERSHEY_PLAIN
    results = tfnet.return_predict(frame)
    helpText="Press 'q' to Quit"
    cv2.putText(frame,'FPS {:.1f}'.format(1 / (time.time() - stime)), (720,20), font, 1.0, (32,32,32), 4, cv2.LINE_AA)
    cv2.putText(frame,'FPS {:.1f}'.format(1 / (time.time() - stime)), (719,20), font, 1.0, (240,240,240), 1, cv2.LINE_AA)
    cv2.putText(frame, helpText, (11,20), font, 1.0, (32,32,32), 4, cv2.LINE_AA)
    cv2.putText(frame, helpText, (10,20), font, 1.0, (240,240,240), 1, cv2.LINE_AA)
    templist = []

    if results == []:
        global list_same_sign
        list_same_sign = []
 
    else:
        list_count = 0
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence=("%.2f"%(result['confidence']*100))
            global label_name
            global same_sign
            if list_same_sign == []:
                pass
            else:
                sign_size = (br[0] - tl[0], br[1] - tl[1])
                for l in list_same_sign:
                    label_name_last_time = l[0]
                    tl_last_time = (l[1], l[2])
                    br_last_time = (l[3], l[4])
                    sign_size_last_time = (br_last_time[0] - tl_last_time[0], br_last_time[1] - tl_last_time[1])
                    
                    if sign_size[0] == sign_size_last_time[0]:
                        size_change = 0
                        size_change_percent = 0
                        check_br_too_far = 0
                        check_tl_too_far = 0
                    else:
                        try:
                            size_change = abs(math.sqrt((sign_size[0]-sign_size_last_time[0])**2 + (sign_size[1]-sign_size_last_time[1])**2))
                            size_change_percent = (size_change / (math.sqrt(sign_size_last_time[0]**2 + sign_size_last_time[1]**2)))*100
                            check_br_too_far = abs(math.sqrt((br[0]-br_last_time[0])**2 + (br[1]-br_last_time[1])**2))
                            check_tl_too_far = abs(math.sqrt((tl[0]-tl_last_time[0])**2 + (tl[1]-tl_last_time[1])**2))
                        except:
                            print("value count error")
                            size_change_percent = 100
                            check_br_too_far = 800
                            check_tl_too_far = 800

                    if label == label_name_last_time:
                        if size_change_percent < 10:
                            if check_br_too_far < 50 or check_tl_too_far < 50:
                                same_sign = True
                                break
            
            label_name = label
            templist.append([])
            templist[list_count].append(label_name)
            templist[list_count].append(tl[0])
            templist[list_count].append(tl[1])
            templist[list_count].append(br[0])
            templist[list_count].append(br[1])
            list_count += 1
                
            frame = cv2.rectangle(frame, tl, br, color, 7)
            frame = cv2.putText(frame, label+" "+str(confidence)+"%", tl, font, 1.0, (32,32,32), 4, cv2.LINE_AA)
            frame = cv2.putText(frame, label+" "+str(confidence)+"%", tl, font, 1.0, (240,240,240), 1, cv2.LINE_AA)
    list_same_sign = templist
    cv2.imshow('PCDemo',frame)
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
        pass
        

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
            
            global flag
            flag = True

        else :
            print("else")
        print ("Exit thread ：" + self.name)
        
        
while True:
    detection()
    if flag:
        if same_sign == False:
            flag = False
            thread1 = myThread(1, "Thread-1", 'play_music', label_name)
            thread1.start()

    same_sign = False
    label_name = None

    if cv2.waitKey(25) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          print('Detection ends.')
          break
    