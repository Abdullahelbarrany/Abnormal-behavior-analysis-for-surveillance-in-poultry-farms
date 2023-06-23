import cv2
import numpy as np
import csv
import pandas as pd
rows = []
xb=yb=0
with open('nofalz.csv', 'r') as csvfile:
    
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        
        rows.append(row)
print(rows[6][0])
#print(len(rows))
# #print(row[0][1])
for j in range(len(rows)):
    blackblankimage = np.full((1000, 1000, 3),(220,220,220), dtype=np.uint8)
    xb=yb=0
    print(len(rows[j]))

    for i in range(1,len(rows[j]),2):
        #print("in")

        xx= int(rows[j][i])
        yy= int(rows[j][i+1])
        # if xx !=xb and yb!=yy:
        blackblankimage= cv2.circle(blackblankimage, (xx,yy), 1, (0, 0, 255), 5 )
        # xb = xx
        # yb=yy
       # cv2.imshow("abood",blackblankimage)
    if rows[j][0] == "eating":
        filename = str(rows[j][0]) + str(j) + ".jpg"
        cv2.imwrite(filename, blackblankimage)
    elif  rows[j][0] == "walking":
        filename = str(rows[j][0]) + str(j) + ".jpg"
        cv2.imwrite(filename, blackblankimage)
    else:
        filename = str(rows[j][0]) + str(j) + ".jpg"
        cv2.imwrite(filename, blackblankimage)

    # cv2.imwrite(str(rows[j][0])+str(j)+".jpg",blackblankimage)


cv2.waitKey(0)
