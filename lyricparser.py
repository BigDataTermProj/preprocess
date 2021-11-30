import csv
import pandas as pd

lyricData = pd.read_csv("/content/drive/MyDrive/BigData_csv/tcc_ceds_music 2.csv",header=None)
# csv 읽기
parsedData=[]

condition = (lyricData[3]=='1985')

lyricData.loc[condition][5]


for i in lyricData.loc[condition][5]:
  parsedData.append(i.split(' '))
print(parsedData)
print(len(parsedData))