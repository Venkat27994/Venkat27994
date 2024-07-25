import csv
import os

df = open("d:\\42309\Desktop\Qlikview\CAPL April 2023 to Feb 2024.csv",'r')
df1 = open("d:\\42309\Desktop\Qlikview\CAPL April 2023 to Feb 2024 empty.csv",'w', newline='')
df2 = open("d:\\42309\Desktop\Qlikview\CAPL April 2023 to Feb 2024 non empty.csv",'w', newline='')

data=csv.reader(df)
wdf1=csv.writer(df1)
wdf2=csv.writer(df2)

for row in data:
    for col in row:
        if col == '':
            wdf1.writerow(row)
            break
    else:
        wdf2.writerow(row)


print("executed succesfully")


print(df) 