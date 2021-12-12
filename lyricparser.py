import csv
import pandas as pd

lyricData = pd.read_csv("/content/drive/MyDrive/BigData_csv/tcc_ceds_music 2.csv",header=None)
# .tsv 읽기
parsedData=[]
result=[]

condition1 = (lyricData[3]=='1985')
condition2 = (lyricData[3]=='1995')
condition3 = (lyricData[3]=='2005')
condition4 = (lyricData[3]=='2015')

for i in lyricData.loc[condition1][5]:
  parsedData.append(i.split(' '))
for i in lyricData.loc[condition2][5]:
  parsedData.append(i.split(' '))
for i in lyricData.loc[condition3][5]:
  parsedData.append(i.split(' '))
for i in lyricData.loc[condition4][5]:
  parsedData.append(i.split(' '))

for i in parsedData:
  for j in range(len(i)):
    result.append(i[j])


print(result)
