"""
@Disha Modi
"""

####
# Steps : 
# 1. Import the required libraries
# 2. Create a VideoCapture object to capture the video from the webcam
# 3. Create a HandDetector object to detect the hands
# 4. Create a variable to store the initial distance between the index finger and the thumb
# 5. Inside the while loop, read the frames from the webcam
# 6. Flip the frame horizontally
# 7. Detect the hands and get the landmarks
# 8. Check if two hands are detected
# 9. If two hands are detected, check if the index finger and the thumb are up for both the hands
# 10. If the index finger and the thumb are up for both the hands, then activate the zoom gesture
# 11. Get the landmarks for the index finger and the thumb for both the hands
# 12. Find the distance between the index finger and the thumb for both the hands
# 13. If the initial distance is None, then set the initial distance to the current distance
# 14. If the initial distance is not None, then find the difference between the current distance and the initial distance
# 15. If the difference is positive, then zoom in
# 16. If the difference is negative, then zoom out
# 17. Display the frame
# 18. Terminate the program if the user presses the escape key
# 19. Release the VideoCapture object
# 20. Destroy all the windows
####

from cvzone.HandTrackingModule import HandDetector
import cv2
import numpy as np
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
origin = None
scale = 0
cx,cy = 500,500


while True:
    success,img = cap.read()
    img = cv2.flip(img,1)
    img,hands = detector.findHands(img)
    image1 = cv2.imread('demo.jpg')
    
    #If two hands are detected, check if the index finger and the thumb are up for both the hands
    if len(hands)==2:
        #We will zoom if first finger and thum are up#
        print(detector.fingersUp(hands[0]),detector.fingersUp(hands[1]))
        if(detector.fingersUp(hands[0]) == [1,1,0,0,0] and detector.fingersUp(hands[1]) == [1,1,0,0,0]):
            print("Zoom Activated")

            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            #Distance between two hands
            #lmList[4] and lmList[8] are the tips of the thumb and index finger
            if origin is None:
                 length,info,img = detector.findDistance(hands[0]['center'],hands[1]['center'],img)
                 print(length)
                 origin = length

            
            # length,info,img = detector.findDistance(lmList1[8],lmList2[8],img)
            length,info,img = detector.findDistance(hands[0]['center'],hands[1]['center'],img)
            scale = int(((length)-(origin))//2)
            cx,cy = info[4:]
            print(scale)
    else:
        print("You can't activate Zoom Gesture as only 1 hand can't zoom")
        origin = None

    try:
        #Resizing image using Zoom Range
        h1,w1,c1 = image1.shape
        newH,newW = int(h1+scale),int(w1+scale)
        image1 = cv2.resize(image1,(newW,newH))
        img[cy-newH//2:cy+newH//2,cx-newW//2:cx+newW//2] = image1
    except:
        pass

    # img[0:500,0:429] = image1
    cv2.imshow("Image",img)
    cv2.waitKey(1)


