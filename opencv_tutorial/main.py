import  numpy as np
import cv2

def desplayingvedio():
    cap = cv2.VideoCapture(0)
    while (cap.isOpened()):
        suc, image = cap.read()
        cv2.imshow("came", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def showimg(img):
    cv2.imshow("image", img)
    k=cv2.waitKey(0)&0xFF
    if k==27:
        cv2.destroyAllWindows()
    elif k==ord('s'):
        cv2.imwrite("/home/v/Downloads/new_image.PNG",img)
        cv2.destroyAllWindows()

img = cv2.imread("/home/v/Downloads/m.jpeg")
img=cv2.resize(img,(512,512))
showimg(img)

desplayingvedio()

blackimg=np.zeros((512,512,3))
blackimg[:,:]=[255,255,255]
showimg(blackimg)

line=cv2.line(blackimg,(0,0),(100,300),(0,0,255),2)
showimg(line)

rectangle=cv2.rectangle(blackimg,(200,200),(265,265),(255,0,255),1)
showimg(rectangle)


############





