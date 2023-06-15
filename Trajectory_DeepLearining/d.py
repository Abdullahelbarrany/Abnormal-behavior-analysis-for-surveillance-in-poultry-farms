import csv
import numpy as np

rows = []

with open('onlyv.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

# csvfile.close() - No need to explicitly close the file when using 'with' statement

rows[0][0] = 877
line = []
arr = np.array(rows, dtype=int)
start = len(arr[0]) // 2
print(start)

with open('nofalz.csv', 'a+', newline='') as f:
    writer = csv.writer(f)

    for j in range(len(arr)):
        x1 = []
        x2 = []
        for i in range(0, start):
            x1.append(str(arr[j][i]))

        for i in range(start, len(arr[j])):
            x2.append(str(arr[j][i]))

        writer.writerow(x1)
        writer.writerow(x2)

# Remove spaces:
