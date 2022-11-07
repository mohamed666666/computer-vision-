import cv2
import numpy as np


def f(x):
    return x



blackimg=np.zeros((512,512,3))
cv2.namedWindow("image")


cv2.createTrackbar("B","image",0,255,f)
cv2.createTrackbar("R","image",0,255,f)
cv2.createTrackbar("G","image",0,255,f)

while True:

    r = cv2.getTrackbarPos('R', "image")
    g = cv2.getTrackbarPos('G', "image")
    blackimg[:] = [b, g, r]
    cv2.imshow("image",blackimg)
    k=cv2.waitKey(0)&0xFF
    if k:
        break



cv2.destroyAllWindows()