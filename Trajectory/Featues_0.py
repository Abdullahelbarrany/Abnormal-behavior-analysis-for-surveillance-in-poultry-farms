import csv
import math
rows=[]
with open('new.csv', 'r') as csvfile:
    
    csvreader = csv.reader(csvfile)
    for row in csvreader:
       
        rows.append(row)
line=[]
lIST_L = []
#print(rows[0][109])
for j in range(len(rows)):
    totx=0
    toty=0
    maxx=-999999999
    maxy=-9999999999
    line = []
    counter=0
    ct=0
   
    line.append(rows[j][0])
    for i in range(1,len(rows[j])-3,4):
        # if rows[j][i] =="," and rows[j][i+1]==",":
        #     print ("in")
        #     break
        # print(rows[j][i])
        totalx=0
        totaly=0
        if i <2:
            fx = int(rows[j][i])
            fy = int(rows[j][i+1])
            line.append(fx)
            line.append(fy)
            totalx+=fx
            totaly+=fy
            # sx=int(rows[j][i])
            # sy = int(rows[j][i+1])
            # #line.append(rows[j][i])
            # #line.append(rows[j][i+1])
        xx= int(rows[j][i])
        yy= int(rows[j][i+1])
        xx2= int(rows[j][i+2])
        yy2= int(rows[j][i+3])
        tx = abs(xx-xx2)
        ty= abs(yy-yy2)
        totalx+= xx
        totalx+=xx2
        totaly+=yy
        totaly+=yy2
           # print("ss")
        if abs(xx2 - xx) <=9 and abs( yy2- yy) <=9:
            counter +=1
          
        # if tx<=100 and ty <=100 :
        totx +=tx
        toty+=ty
        if tx>maxx:
            maxx=tx
        if ty >maxy:
            maxy=ty 
        ct+=1
    ct = ct/2       
    meanx = totalx / ct
    meany  = totaly / ct
    line.append(totx)

    line.append(toty)
    line.append(xx2)
    line.append(yy2)
    # line.append(len(rows[j])-1)
    ######################################################################################################################appending diff
    
    line.append(maxx)
    line.append(maxy)
    counter = counter/ct
    counter = counter*100
    line.append(counter)
    lIST_L.append(line)
    line.append(meanx)
    line.append(meany)
    line = []
with open('try2.csv', 'a+') as f:
    writer = csv.writer(f)
    for i in lIST_L:
        writer.writerow(i)
    f.close()