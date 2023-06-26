"""
@Disha Modi
"""
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
ret,frame2 = cap.read()
while cap.isOpened():
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    #Why we use blur? -> To remove noise. 
    blur = cv2.GaussianBlur(gray,(5,5),0) #to remove noise
    #Why we use threshold? -> To convert the image into binary form.
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    #Why we use dilate? -> To fill holes.
    dilated = cv2.dilate(thresh,None,iterations=3) #to fill holes
    #Why we use contours? -> To draw the boundaries of the object.
    contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame1,contours,-1,(0,255,0),2)

    cv2.imshow("feed",frame1)
    #We use equal sign because we want to update the frame1.
    frame1 = frame2

    ret,frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break
cv2.destroyAllWindows()
cap.release()

