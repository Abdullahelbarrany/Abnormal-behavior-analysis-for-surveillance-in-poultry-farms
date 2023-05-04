import numpy as np

# with open("onlyv.csv",encoding="utf-8-sig") as file_name:
#     array = np.loadtxt(file_name, delimiter=",")

# print(array)
import csv
from scipy.stats import skew
import statistics
rows=[]
with open('onlyv.csv', 'r') as csvfile:
    
    csvreader = csv.reader(csvfile)
    for row in csvreader:
       
        rows.append(row)
# with open("onlyv.csv") as file_name:
#     file_read = csv.reader(file_name)

    # array = list(file_read)
    # array[0][0]=877
    rows[0][0]= 877
    arr= np.array(rows[0],dtype=float)
    #print(np.mean(arr))
    #print("the standard deviation is " + (statistics.stdev(arr)))
    min = np.amin(arr)
    print(min)
    for j in range(len(rows)):
        line = []
        arr= np.array(rows[j],dtype=float)
        mean = np.mean(arr)
        line.append(mean)
        std= np.std(arr)
        line.append(std)
        min = np.amin(arr)
        max=np.amax(arr)
        line.append(min)
        line.append(max)
        median= np.median(arr)
        line.append(median)
        co_of_variation= std / mean
        line.append(co_of_variation)
        p2pamplitude=max-min
        line.append(p2pamplitude)
        #percentile = np.percentile(arr,50)
        #print(np.mean(arr)) 
        sk = 3*(mean-median)
        sk = sk / std
        line.append(sk)
        with open('allnew.csv', 'a+') as f:
            writer = csv.writer(f)
           
            writer.writerow(line)
        f.close()
csvfile.close()