import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#edge detection by laplacian method
lap=cv2.Laplacian(img,cv2.CV_64F)
lap=np.uint8(np.absolute(lap))
#edge detection by sobel
soblx=cv2.Sobel(img,cv2.CV_64F,0,1)
soblx=np.uint8(np.absolute(soblx))

sobely=cv2.Sobel(img,cv2.CV_64F,1,0)
sobely=np.uint8(np.absolute(sobely))

Sobel=cv2.bitwise_or(sobely,soblx)

#using canny

edges=cv2.Canny(img,100,100)

img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# displaying my images
titles = ['image','Laplacian','Sobelx',"Sobely","Soble","Canny","GRAy"]
images = [img,lap,soblx,sobely,Sobel,edges,img2]

for i in range(7):
    plt.subplot(4, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

##test
img = cv2.imread('lena.jpg')
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("mn",img2)
cv2.waitKey(0)
cv2.imshow("out1",img)
cv2.waitKey(0)
print(img2.shape)

img2=cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)
print(img2.shape)
cv2.imshow("out",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()