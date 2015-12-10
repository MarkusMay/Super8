import cv2
import numpy as np

img = cv2.imread('images.jpeg',0)
ret,thresh = cv2.threshold(img,217,255,0)
img,contours,hierarchy = cv2.findContours(thresh, 1,2)

cnt = contours[0]
M = cv2.moments(cnt)
print M


epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

print epsilon
print approx

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img,[box],0,(50,51,255),2)
cv2.ShowImage("quelle", img)
