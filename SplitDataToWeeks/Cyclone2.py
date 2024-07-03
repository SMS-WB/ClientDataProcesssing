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



filename_in = 'cycloneData.txt'
print(f'Opening {filename_in}')

with open(filename_in,'r') as file_in:
	print(f'Loading Header Data')
	all_data 	= [line.strip() for line in file_in.readlines()]
	columnTitles= all_data[0]

	startTime = all_data[1].strip()

	startTimeReadable = datetime.datetime.fromtimestamp(startTime_s)
	startDayNumber = int(startTimeReadable.weekday())
	startDay =daysOfWeek[startTimeReadable.weekday()]
	print(f'{startTimeReadable} ({startDay})')

	startWeek_wc = datetime.datetime.fromtimestamp(startTime_s-startDayNumber*86400)
	print(startWeek_wc)

print(f'Loading Acoustic Data')
data   = np.loadtxt(filename_in,delimiter='\t',skiprows=21,dtype=float)

#print(data[0][0])
week = 0
previousDay = startDayNumber

data_dims = data.shape
#print(data_dims[0])
wc = startWeek_wc

start_time = time.time()

fileout = f"{sensorTag} WC {wc.date()}.txt"
fo = open(fileout,"w")

for row in range(1,data_dims[0]):
	currentDate = datetime.datetime.fromtimestamp(startTime_s+data[row][0]/1000)
	currentDay = currentDate.weekday()
	currentDayName = daysOfWeek[currentDate.weekday()]
	if currentDay<previousDay:
		week = week + 1
		previousDay = currentDay
		wc = currentDate
		fo.close
		fileout = f"{sensorTag} WC {wc.date()}.txt"
		fo = open(fileout,"w")
#	print(f'{row}:\t{currentDayName} (Week {week}, WC {wc})\t{currentDate},\t{data[row][1]}\t{data[row][2]}')

	fo.write(f'{currentDate}\t{data[row][1]}\t{data[row][2]}\n')

print(f'--- {week+1} weeks, {round(time.time() - start_time)} seconds ---')
