"""
@Disha Modi
"""
import cv2
eventscv =  [i for i in dir(cv2) if 'EVENT' in i]
print(eventscv)
