"""
@Disha Modi
"""
import cv2
import numpy as np

img = np.zeros([512,512,3],np.uint8)

def clickevent(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(255,255,255),1)
        points.append((x,y))
        if(len(points)>=2):
            cv2.line(img,points[-1],points[-2],(0,0,0),2);
        cv2.imshow('image',img)

img = cv2.imread('lena.png',1)
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image',clickevent)

cv2.waitKey(0)
cv2.destroyAllWindows()
