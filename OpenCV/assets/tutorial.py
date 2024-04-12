import cv2
img=cv2.imread('assets/logo.jpg',0)
img=cv2.resize(img,(0,0),fx=2,fy=2) #resize the image giving image name and pixels and fx and fy scale the image making it 2x,3x its size
#rotating image
img=cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#display image
cv2.imshow('Image',img)
cv2.waitKey(0) #0 means wait infinitely
cv2.destroyAllWindows()

