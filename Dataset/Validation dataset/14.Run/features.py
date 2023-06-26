import numpy as np
import csv
from scipy.stats import skew
import statistics
correct=0
for i in range(1,146):
    count = 0
    rows=[]

    if i==131:
        continue
    # print(i)
    with open('run ('+str(i)+').csv', 'r') as csvfile:
        
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if count>=600:
                break
            else:

                rows.append(row)
                count+=1


        csvfile.close()
    #rows[0][0]= 877
    arr= np.array(rows,dtype=float)
    if len(arr) <600:
        continue
    e_distance= 0
    line=[]
    max_distance=-9999999999999
    standingstill=0
    startingx = 0
    startingy= 0
    startingz=0
    endingx= endingy=endingz=0
    for i in range(0,len(arr),2):
        x = arr[i][1]
        y = arr[i][2]
        z = arr[i][3]
        x2 = arr[i+1][1]
        y2 = arr[i+1][2]
        z2 = arr[i+1][3]
        endingx += x+x2
        endingy+=y+y2
        endingz+=z+z2
        p1 = np.array((x,y,z))
        p2 = np.array((x2,y2,z2))
        e_distance += np.linalg.norm(p1 - p2)
        d_each_step = np.linalg.norm(p1 - p2)
        if d_each_step<=0.5:
                standingstill+=1
        if max_distance<d_each_step:
                max_distance = d_each_step
    #########################################################################
    mean = e_distance / (len(arr))
    std= np.std(arr)
    
    co_of_variation= std / mean
    # endingx = arr[len(arr)-1][1]
    # endingy = arr[len(arr)-1][2]
    # endingz = arr[len(arr)-1][3]
    p1 = np.array((startingx,startingy,startingz))
    p2 = np.array((endingx,endingy,startingz))
    s_e_pos=np.linalg.norm(p1 - p2)
 
    line.append(standingstill)
    line.append(e_distance)
    line.append(mean)
    line.append(max_distance)
    

    line.append(s_e_pos)
    line.append('Run')
   
    with open('human.csv', 'a+') as f:
            writer = csv.writer(f)
        
            writer.writerow(line)
    f.close()










    




