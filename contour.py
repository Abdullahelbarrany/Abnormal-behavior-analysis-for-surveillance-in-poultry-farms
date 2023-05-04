# import PIL
# from PIL import Image
# img = Image.open('s1.png')
# img = img.convert('RGB')
# #img.show()
# for x in range(img.size[0]):
#     for y in range(img.size[1]):
#         r, g, b = img.getpixel((x,y))
#         if(r>240 and g>240 and b>238):
#             img.putpixel((x,y),(0,0,0))
# img.show()
# from ctypes.wintypes import SIZE
import cv2
size =(500,373)
img = cv2.imread('s1.png')
ref = cv2.resize(img,size,interpolation = cv2.INTER_AREA)
#cv2.imshow("resized",ref)

new = cv2.imread('s2.jpg')
result = cv2.subtract(ref,new)
cv2.imshow("result pic",result)
cv2.waitKey(0)
# import cv2
# import numpy as np
# img = cv2.imread('s2.jpg')
# blurred_frame = cv2.GaussianBlur(img, (5, 5), 0)
# hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
# lower_blue = np.array([108, 87, 44])
# upper_blue = np.array([84,59, 29])
# mask = cv2.inRange(img, lower_blue, upper_blue)
# cv2.imshow('mask',mask)
# cv2.imshow('ttt',img)
# cv2.waitKey(0)