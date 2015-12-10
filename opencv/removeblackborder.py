import copy
import cv2

from matplotlib import pyplot as plt


IMG_IN = 'frame1.jpeg'


# keep a copy of original image
original = cv2.imread(IMG_IN)

# Read the image, convert it into grayscale, and make in binary image for threshold value of 1.
img = cv2.imread(IMG_IN,0)

# use binary threshold, all pixel that are beyond 3 are made white
_, thresh_original = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY)

# Now find contours in it.
thresh = copy.copy(thresh_original)
_, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# get contours with highest height
lst_contours = []
for cnt in contours:
    ctr = cv2.boundingRect(cnt)
    lst_contours.append(ctr)
x,y,w,h = sorted(lst_contours, key=lambda coef: coef[3])[-1]


# draw contours
ctr = copy.copy(original)
cv2.rectangle(ctr, (x,y),(x+w,y+h),(0,255,0),2)

#crop image
crop = original[y:y+h,x:x+w]
cv2.imwrite('frame_edit.jpeg',crop)

# display results with matplotlib

# original
original = original[:,:,::-1] # flip color for maptolib display
plt.subplot(221), plt.imshow(original)
plt.title('Original Image'), plt.xticks([]),plt.yticks([])

# Threshold
plt.subplot(222), plt.imshow(thresh_original, cmap='gray')
plt.title('threshold binary'), plt.xticks([]),plt.yticks([])

# selected area for future crop
ctr = ctr[:,:,::-1] # flip color for maptolib display
plt.subplot(223), plt.imshow(ctr)
plt.title('Selected area'), plt.xticks([]),plt.yticks([])

plt.show()
