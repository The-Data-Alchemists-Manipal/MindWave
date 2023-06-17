"""
@Disha Modi
"""
import cv2
import datetime
cap = cv2.VideoCapture(0)
while(cap.isOpened):
    ret,frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        #To get the date and time of the system
        dateandtime = str(datetime.datetime.now()) 
        frame = cv2.putText(frame,dateandtime,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

    else:
        break