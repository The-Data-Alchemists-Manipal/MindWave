"""
@ Disha Modi
"""

import cv2
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID') # XVID is the codec
#fourcc = cv2.VideoWriter_fourcc('X','V','I','D') # XVID is the codec

out = cv2.VideoWriter('output.avi',fourcc,120.0,(640,480)) # 20.0 is the frame rate, (640,480) is the size of the frame
print(cap.isOpened())
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret== True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # get the width of the frame
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   # get the height of the frame
        out.write(frame) # write the frame to the output file
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()