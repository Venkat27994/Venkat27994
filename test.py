import csv
import os

df = open("d:\\42309\Desktop\Qlikview\CAPL April 2023 to Feb 2024.csv",'r')
df1 = open("d:\\42309\Desktop\Qlikview\CAPL April 2023 to Feb 2024 error.csv",'w', newline='')
df2 = open("d:\\42309\Desktop\Qlikview\CAPL April 2023 to Feb 2024 correction.csv",'w', newline='')

data=csv.reader(df)
wdf1=csv.writer(df1)
wdf2=csv.writer(df2)

for row in data:
    if '-' in row[15]:
        wdf2.writerow(row)
    else:
        wdf1.writerow(row)

print("executed succesfully")


print(df) 