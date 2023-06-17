import cv2 as cv
import numpy as np

img = cv.imread('smarties.jpg')
output = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
#cv.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]])
#image : 8-bit, single-channel, grayscale input image.
#circles : Output vector of found circles. Each vector is encoded as a 3-element floating-point vector (x, y, radius) .
#method : Detection method to use. Currently, the only implemented method is HOUGH_GRADIENT , which is basically 21HT , described in [Yuen90].
#dp : Inverse ratio of the accumulator resolution to the image resolution. For example, if dp=1 , the accumulator has the same resolution as the input image. If dp=2 , the accumulator has half as big width and height.
#minDist : Minimum distance between the centers of the detected circles. If the parameter is too small, multiple neighbor circles may be falsely detected in addition to a true one. If it is too large, some circles may be missed.
#param1 : First method-specific parameter. In case of HOUGH_GRADIENT , it is the higher threshold of the two passed to the Canny edge detector (the lower one is twice smaller).
#param2 : Second method-specific parameter. In case of HOUGH_GRADIENT , it is the accumulator threshold for the circle centers at the detection stage. The smaller it is, the more false circles may be detected. Circles, corresponding to the larger accumulator values, will be returned first.
#minRadius : Minimum circle radius.
#maxRadius : Maximum circle radius. If <= 0, uses the maximum image dimension. If < 0, returns centers without finding the radius.

circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20,
                            param1=50, param2=30, minRadius=0, maxRadius=0)   
      
detected_circles = np.uint16(np.around(circles))

for (x, y ,r) in detected_circles[0, :]:
    cv.circle(output, (x, y), r, (0, 255, 0), 3)
    cv.circle(output, (x, y), 2, (0, 255, 255), 3)

cv.imshow('output', output)
cv.waitKey(0)
cv.destroyAllWindows()
