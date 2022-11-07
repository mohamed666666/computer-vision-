import numpy as np
import cv2

img = cv2.imread('opencv.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,127,255,0)
contours,hairarchi=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img,contours,-1,(125,125,25),2)



cv2.imshow("image",img)
cv2.waitKey(0)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()