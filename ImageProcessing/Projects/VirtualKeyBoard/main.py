"""
@Disha Modi
"""
###############################Virtual Keyboard##########################################
#1. Create the buttons
#2. Draw the buttons
#3. Check if the hand is in the button rectangle
#4. Click the button
#5. Create the rectangle for the final text
#6. Add the keyclicked to the final text
#7. Display the final text
##########################################################################################
import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import numpy as np
import time
import os

cap = cv2.VideoCapture(0)
cap.set(3,10280)
cap.set(4,1720)

detector = HandDetector(detectionCon=0)

keys = [
        ["Q","W","E","R","T","Y","U","I","O","P"],
        ["A","S","D","F","G","H","J","K","L",";"],
        ["Z","X","C","V","B","N","M",",",".","/"]
        ]

finaltext = ""

#Draw the buttons
def drawAll(img, buttonList):
    for button in buttonList:
        x,y = button.pos
        w,h = button.size
        cv2.rectangle(img, button.pos, (x+w,y+h), (255,0,255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 4)
    return img

class KeyButton():
    def __init__(self, pos, text, size=[85,85]):
        self.pos = pos
        self.size = size
        self.text = text

    # def draw(self, img):
    #     #pos - (x,y) coordinates of the top left corner of the rectangle
    #     #size - (width, height) of the rectangle
    #     x,y = self.pos
    #     m,n = self.size
    #     cv2.rectangle(img, self.pos, (x+m,y+n), (255,0,255), cv2.FILLED)
    #     cv2.putText(img, self.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 4)
    #     return img

buttonList = []
alphabet = KeyButton([100,100], "Q")


while True:
    success, img = cap.read()
    img = detector.findHands(img)   #To find hands
    lmList, bboxInfo = detector.findPosition(img)   #To find landmarks

    for i in range(len(keys)):
        for j,key in enumerate(keys[i]):
            buttonList.append(KeyButton([100*j+50,100*i], key))

    #To create the images in each frame.
    # img = alphabet.draw(img)
    img = drawAll(img, buttonList)

    if lmList:
        #To check if in buttonList
        for button in buttonList:
            x,y = button.pos
            w,h = button.size

            #To check if the hand is in the button rectangle
            if x < lmList[8][0] < x+w and y < lmList[8][1] < y+h:
                cv2.rectangle(img, button.pos, (x+w,y+h), (175,0,175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 4)
                l,_,_ = detector.findDistance(8,12,img, draw=False)  #To find the distance between the index and middle finger
                print(l)

                #To click the button
                if l<30:
                    #To check if the button is clickeds
                    cv2.rectangle(img, button.pos, (x+w,y+h), (0,255,0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 4)
                    finaltext += button.text    #To add the keyclicked to the final text
                    time.sleep(0.15)
                
    #To create the rectangle for the final text
    cv2.rectangle(img, (50,350), (700,450), (175,0,175), cv2.FILLED)
    cv2.putText(img, finaltext, (60,430), cv2.FONT_HERSHEY_PLAIN, 5, (255,255,255), 5)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

 
