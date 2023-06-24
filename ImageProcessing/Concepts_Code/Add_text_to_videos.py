"""
@Disha Modi
"""

import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,1208) # 3 is the flag for width
cap.set(4,720) # 4 is the flag for height
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret== True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+str(cap.get(3))+' Height: '+str(cap.get(4))
        frame = cv2.putText(frame,text,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
