# Sand Data Converter
# 2023-08-31

import sys
import math
import os
from array import *
import numpy as np
import matplotlib as matplotlib
import matplotlib.pyplot as plt
import re
import datetime
import time
daysOfWeek = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']



cyclone_in = 'cycloneData.txt'

with open(cyclone_in,'r') as ci:
	print(f'Loading Cyclone Column Titles')
	all_data 	= [line.strip() for line in ci.readlines()]
	CycloneColumnTitles = all_data[0]
	remainderCycloneData = all_data[1:]
	cycloneTitles = CycloneColumnTitles.split('\t')
	#chokeData   = np.loadtxt(ci,delimiter='\t',skiprows=1,dtype=str,unpack=True)

lines = len(remainderCycloneData)

cycloneData = list()

firstLine = remainderCycloneData[0].split('\t')
startTime = firstLine[0]
theStartTime = datetime.datetime.strptime(startTime,'%d/%m/%Y %H:%M')

startDayNumber = int(theStartTime.weekday())
startDay =daysOfWeek[theStartTime.weekday()]
print(f'{theStartTime} ({startDay})')
startWeek_wc = datetime.datetime.fromtimestamp(time.mktime(theStartTime.timetuple())-startDayNumber*86400)
print(startWeek_wc)

currentDate = theStartTime
currentDay = currentDate.weekday()



for i in range(0,lines):
	cycloneData.append(remainderCycloneData[i].split('\t'))


# Cyclone Columns
#	0	Time
#	1	Well 1: 20-CE-012 DeltaP
#	2	Well 2: 20-CE-010 DeltaP
#	3	Well 3: 20-CE-014 DeltaP






week = 0
previousDay = currentDay
wc = startWeek_wc
start_time = time.time()

fa00 = open(f"Well 1 - wc {wc.date()}.txt",'w')
fa01 = open(f"Well 2 - wc {wc.date()}.txt",'w')
fa02 = open(f"Well 3 - wc {wc.date()}.txt",'w')

fa00.write(f'{cycloneTitles[0]}\t{cycloneTitles[1]}\n')
fa01.write(f'{cycloneTitles[0]}\t{cycloneTitles[2]}\n')
fa02.write(f'{cycloneTitles[0]}\t{cycloneTitles[3]}\n')

for i in range(0, lines):
	currentDate = datetime.datetime.strptime(cycloneData[i][0],'%d/%m/%Y %H:%M')
	currentDay = currentDate.weekday()
	currentDayName = daysOfWeek[currentDay]

	if currentDay<previousDay:
		week = week+1
		previousDay = currentDay
		wc = currentDate
		fa00.close()
		fa01.close()
		fa02.close()

		fa00 = open(f"Well 1 - wc {wc.date()}.txt",'w')
		fa01 = open(f"Well 2 - wc {wc.date()}.txt",'w')
		fa02 = open(f"Well 3 - wc {wc.date()}.txt",'w')
		fa00.write(f'{cycloneTitles[0]}\t{cycloneTitles[1]}\n')
		fa01.write(f'{cycloneTitles[0]}\t{cycloneTitles[2]}\n')
		fa02.write(f'{cycloneTitles[0]}\t{cycloneTitles[3]}\n')

	fa00.write(f'{cycloneData[i][0]}\t{cycloneData[i][1]}\n')
	fa02.write(f'{cycloneData[i][0]}\t{cycloneData[i][2]}\n')
	fa01.write(f'{cycloneData[i][0]}\t{cycloneData[i][3]}\n')
	print(f'{previousDay}\t{currentDay}')
	#print(f'{i}:\t{currentDayName} (Week {week}, WC {wc})\t{currentDate},\t{cycloneData[i][1]}\t{cycloneData[i][2]}\t{cycloneData[i][3]}')
	#print(f'Writing Line {i} of {lines}')
	previousDay = currentDay

fa00.close()
fa01.close()
fa02.close()


#startTimeReadable = datetime.datetime.fromtimestamp(startTime_s)
#startDayNumber = int(startTimeReadable.weekday())
#startDay =daysOfWeek[startTimeReadable.weekday()]
#print(f'{startTimeReadable} ({startDay})')
#startWeek_wc = datetime.datetime.fromtimestamp(startTime_s-startDayNumber*86400)
#print(startWeek_wc)

#print(f'Loading Acoustic Data')

#print(data[0][0])
#week = 0
#previousDay = startDayNumber

#data_dims = data.shape
#print(data_dims[0])
#wc = startWeek_wc

#start_time = time.time()

#fileout = f"{sensorTag} WC {wc.date()}.txt"
#fo = open(fileout,"w")

#for row in range(1,data_dims[0]):
#	currentDate = datetime.datetime.fromtimestamp(startTime_s+data[row][0]/1000)
#	currentDay = currentDate.weekday()
#	currentDayName = daysOfWeek[currentDate.weekday()]
#	if currentDay<previousDay:
#		week = week + 1
#		previousDay = currentDay
#		wc = currentDate
#		fo.close
#		fileout = f"{sensorTag} WC {wc.date()}.txt"
#		fo = open(fileout,"w")
#	print(f'{row}:\t{currentDayName} (Week {week}, WC {wc})\t{currentDate},\t{data[row][1]}\t{data[row][2]}')

#	fo.write(f'{currentDate}\t{data[row][1]}\t{data[row][2]}\n')

#print(f'--- {week+1} weeks, {round(time.time() - start_time)} seconds ---')
