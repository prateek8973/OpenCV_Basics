import cv2
import random
img=cv2.imread('assets/logo.jpg',-1)
tag=img[1:4,3:4]
img[8:11,5:6]=tag 

#manipulating pixels in an image
#for i in range(40):
#    for j in range(img.shape[1]):
#        img[i][j]=[random.randint(0,120),random.randint(0,255),random.randint(0,255)]
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



#print(img.shape) #shows (height,width,channel)
#OpenCV uses BGR[blue,green,red] by default
# 0 means none and 255 means all 

