import cv2
import numpy as np
import csv
import pandas as pd
rows = []
xb=yb=0
with open('ph.csv', 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    for row in csvreader:

        rows.append(row)

# print(len(rows))
print(int(float(rows[2][0])))
# print(rows[1][1])
blackblankimage = np.zeros(shape=[1000, 1400, 3], dtype=np.uint8)
l=[]
for j in range(2,len(rows)):
    if j==2:
        continue
    xb=yb=0

    xx= int(float(rows[j][0]))-int(float(rows[2][0]))
    yy= int(float(rows[j][1]))

    xx1 = int(float(rows[j-1][0]))-int(float(rows[2][0]))
    yy1 = int(float(rows[j-1][1]))
    # if xx !=xb and yb!=yy:
    img =cv2.line(blackblankimage,(xx,yy),(xx1,yy1), (255, 0, 0),2)
    #print (a)
    # xb = xx
    # yb=yy
    # cv2.imshow("abood",blackblankimage)



cv2.imwrite(rows[j][0]+str(j)+".jpg",img)
cv2.waitKey(0)