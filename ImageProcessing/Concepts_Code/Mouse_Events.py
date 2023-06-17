"""
@Disha Modi
"""
import cv2
import numpy as np

img = np.zeros([512,512,3],np.uint8)
#img = cv2.imread('lena.png',1)

def clickevent(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN :
        print(x,',',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x)+','+str(y)
        cv2.putText(img,strXY,(x,y),font,1,(255,255,0),2)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue)+','+str(green)+','+str(red)
        cv2.putText(img,strBGR,(x,y),font,1,(0,255,255),2)
        cv2.imshow('image',img)

img = cv2.imread('lena.png',1)
cv2.imshow('image',img)

cv2.setMouseCallback('image',clickevent)

cv2.waitKey(0)
cv2.destroyAllWindows()