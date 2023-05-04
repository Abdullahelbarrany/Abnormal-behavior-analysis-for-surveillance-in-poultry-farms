import numpy as np
import csv
from scipy.stats import skew
import statistics
rows=[]

with open('onlyv.csv', 'r') as csvfile:
    
    csvreader = csv.reader(csvfile)
    for row in csvreader:
       
        rows.append(row)

    csvfile.close()
rows[0][0]= 877
arr= np.array(rows,dtype=float)

for i in range(len(arr)):
    e_distance= 0
    line=[]
    max_distance=-9999999999999
    standingstill=0
    startingx = arr[i][0]
    startingy= arr[i][1]
    for j in range(0,len(arr[i]),4):
       x = arr[i][j]
       y = arr[i][j+1]
       x2 = arr[i][j+2]
       y2= arr[i][j+3]
       p1 = np.array((x,y))
       p2 = np.array((x2,y2))
       e_distance += np.linalg.norm(p1 - p2)
       d_each_step = np.linalg.norm(p1 - p2)
       if d_each_step<=10:
            standingstill+=1
       if max_distance<d_each_step:
            max_distance = d_each_step
    mean = e_distance / (len(arr[i]))
    std= np.std(arr[i])
    #min = np.amin(arr)
    #max=np.amax(arr)
    #line.append(min)
    #line.append(max)
    #median= np.median(arr[i])
    # line.append(median)
    co_of_variation= std / mean
    #p2pamplitude=max-min
    #sk = 3*(mean-median)
    #sk = sk / std
   
    endingx = arr[i][len(arr[i])-2]
    endingy = arr[i][len(arr[i])-1]
    p1 = np.array((startingx,startingy))
    p2 = np.array((endingx,endingy))
    s_e_pos=np.linalg.norm(p1 - p2)
    #line.append(startingx)
    #line.append(startingy)
    #line.append(endingx) 
    #line.append(endingy)
    line.append(standingstill)
    line.append(e_distance)
    line.append(mean)
    line.append(max_distance)

    line.append(s_e_pos)
    #line.append(std)
    #line.append(co_of_variation)
    #line.append[p2pamplitude]
    #line.append(sk)
    with open('human.csv', 'a+') as f:
            writer = csv.writer(f)
           
            writer.writerow(line)
    f.close()










    




