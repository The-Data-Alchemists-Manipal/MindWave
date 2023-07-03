"""
@Disha Modi
"""

#STEPS TO FULFILL : #
############
#   1. Find Hand Landmarks
#   2. Get the tip of the index and middle fingers
#   3. Check which fingers are up
#   4. Only Index Finger : Moving Mode
#   5. Convert Coordinates
#   6. Smoothen Values
#   7. Move Mouse
#   8. Both Index and middle fingers are up : Clicking Mode
#   9. Find distance between fingers
#   10. Click mouse if distance short
#   11. Frame Rate
#   12. Display
############

import cv2
import numpy as np
import cvzone
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector as htm
import time
import autopy

#####Getting the variables######
widthCam,heightCam = 640,480
widthScreen,heightScreen = autopy.screen.size()
previousTime = 0   #For frame rate
frameR = 100   #Frame Reduction
smoothening = 7   #Smoothening the mouse movement
plocX,plocY = 0,0   #Previous location of the mouse
clocX,clocY = 0,0   #Current location of the mouse
###########

# Webcam
cap = cv2.VideoCapture(0)
# Set width and height
cap.set(3, 640)
cap.set(4, 480)
detector = htm.handDetector(maxHands=1,detectionCon=0.7)
while True:
    #1. Find Hand Landmarks
    success,img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    #2. Get the tip of the index and middle fingers
    if len(lmList)!=0:
        #The numbers 8,12 are the tip of the index and middle fingers respectively
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]
        print(x1,y1,x2,y2)
    

    #3. Check which fingers are up
    fingers = detector.fingersUp()
    print(fingers)

    cv2.rectangle(img,(frameR,frameR),(widthCam-frameR,heightCam-frameR),(255,0,255),2)   #Drawing a rectangle in the middle of the screen

    #4. Only Index Finger : Moving Mode
    #fingers[1] is the index finger
    #fingers[2] is the middle finger
    if fingers[1]==1 and fingers[2]==0:    #If index finger is up and middle finger is down, that is moving mode
        #5. Convert Coordinates
        x3 = np.interp(x1,(frameR,widthCam-frameR),(0,widthScreen))   #Converting the coordinates of the webcam to the coordinates of the screen
        y3 = np.interp(y1,(frameR,heightCam-frameR),(0,heightScreen))   #Converting the coordinates of the webcam to the coordinates of the screen
        #6. Smoothen Values
        clocX = plocX + (x3-plocX)/smoothening   #Smoothening the x coordinate of the mouse
        clocY = plocY + (y3-plocY)/smoothening   #Smoothening the y coordinate of the mouse
        #7. Move Mouse
        autopy.mouse.move(widthScreen-x3,y3)    #Moving the mouse to the coordinates of the index finger
        cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)   #Drawing a circle at the tip of the index finger
        plocX,plocY = clocX,clocY   #Updating the previous location of the mouse

    #8. Both Index and middle fingers are up : Clicking Mode
    if fingers[1]==1 and fingers[2]==1:    #If index finger and middle finger are up, that is clicking mode
        #9. Find distance between fingers
        length, img, lineInfo = detector.findDistance(8,12,img) #8,12 are the tip of the index and middle fingers respectively
        print(length)
        #10. Click mouse if distance short
        if length<40:
            cv2.circle(img,(lineInfo[4],lineInfo[5]),15,(0,255,0),cv2.FILLED)
            autopy.mouse.click()    #Clicking the mouse
        
    #11. Frame Rate
    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    #12. Display
    cv2.imshow("Image",img)
    cv2.waitKey(1)
