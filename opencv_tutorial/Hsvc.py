import cv2
import numpy as np
def f(x):
    pass
"""while True:
    frame=cv2.imread("/home/v/Downloads/coloredBalls.jpg")
    img=cv2.resize(frame,(680,512))
    cv2.namedWindow("image")
    #create track bares
    cv2.createTrackbar("R","image",0,255,f)
    cv2.createTrackbar("G","image",0,255,f)
    cv2.createTrackbar("B","image",0,255,f)

    #resize the pic
    frame=cv2.resize(frame,(688,512))

    #show pic
    cv2.imshow("image",frame)
    cv2.waitKey(0)

    #get track bar values
    b = cv2.getTrackbarPos("B", "image")
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    print("b :"+str(b))
    print("r :"+str(r))
    print("g :"+str(g))
    ### edit our pic

    frame[:]=[b,g,r]
    cv2.imshow("output",frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #############
"""""
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking",0,255,f)
cv2.createTrackbar("UH","Tracking",255,255,f)
cv2.createTrackbar("LS","Tracking",0,255,f)
cv2.createTrackbar("US","Tracking",255,255,f)
cv2.createTrackbar("LV","Tracking",0,255,f)
cv2.createTrackbar("UV","Tracking",255,255,f)


while True:
    frame = cv2.imread("/home/v/Downloads/coloredBalls.jpg")
    frame=cv2.resize(frame,(300,220))

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos("LH","Tracking")
    u_h=cv2.getTrackbarPos("UH","Tracking")
    l_s=cv2.getTrackbarPos("LS","Tracking")
    u_s=cv2.getTrackbarPos("US","Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv,l_b,u_b)

    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
cv2.destroyAllWindows()




