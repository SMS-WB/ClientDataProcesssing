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



choke_in = 'choke.txt'
flow_in = 'flowrate.txt'
pressure_and_temperature_in = 'PressureTemperature.txt'
#print(f'Opening {filename_in}')

with open(choke_in,'r') as ci:
	print(f'Loading Choke Column Titles')
	all_data 	= [line.strip() for line in ci.readlines()]
	ChokeColumnTitles = all_data[0]
	remainderChokeData = all_data[1:]
	chokeTitles = ChokeColumnTitles.split('\t')
	#chokeData   = np.loadtxt(ci,delimiter='\t',skiprows=1,dtype=str,unpack=True)

with open(flow_in,'r') as fi:
	print(f'Loading Flow Column Titles')
	all_data 	= [line.strip() for line in fi.readlines()]
	FlowColumnTitles = all_data[0]
	remainderFlowData = all_data[1:]
	flowTitles = FlowColumnTitles.split('\t')
	#flowData = np.loadtxt(fi,delimiter='\t',skiprows=1,dtype=str,unpack=True)

with open(pressure_and_temperature_in,'r') as pti:
	print(f'Loading Pressure/Temperature Column Titles')
	all_data 	= [line.strip() for line in pti.readlines()]
	PressureTemperatureColumnTitles = all_data[0]
	remainderPtData = all_data[1:]
	ptTitles = PressureTemperatureColumnTitles.split('\t')
	#ptData = np.loadtxt(pti,delimiter='\t',skiprows=1,dtype=str,unpack=True)

lines = len(remainderPtData)

flowData = list()
chokeData = list()
ptData = list()
#flowData = np.empty(lines,dtype=str)
#chokeData = np.empty(lines,dtype=str)
#ptData = np.empty(lines,dtype=str)

for i in range(0,lines):
	flowData.append(remainderFlowData[i].split('\t'))
	chokeData.append(remainderChokeData[i].split('\t'))
	ptData.append(remainderPtData[i].split('\t'))

fa00 = open("Sensors Relating to B1-18-AE-0210.txt",'w')
fa01 = open("Sensors Relating to B1-27-AE-0220.txt",'w')
fa02 = open("Sensors Relating to B2-18-AE-0110.txt",'w')
fa03 = open("Sensors Relating to B2-27-AE-0120.txt",'w')
#fa04 = open("Sensors Relating to B1-18-AE-0210.txt",'w')
fa05 = open("Sensors Relating to B3-27-AE-0320.txt",'w')
fa06 = open("Sensors Relating to B4-18-AE-0610.txt",'w')
fa07 = open("Sensors Relating to B4-27-AE-0620.txt",'w')
fa08 = open("Sensors Relating to B5-18-AE-0410.txt",'w')
fa09 = open("Sensors Relating to B5-27-AE-0420.txt",'w')
fa10 = open("Sensors Relating to 18-AT-0310.txt",'w')

# Flowrate Columns: 
#	0	TimeDate	
#	1	VMS_BB_BA_27_FI_4706	
#	2	VMS_BB_BA_27_FI_4700	
#	3	VMS_BB_BA_27_FI_4712	
#	4	VMS_BB_BA_27_FI_4724	
#	5	VMS_BB_BA_27_FI_4718
# Choke Columns:	
#	0	TimeDate	
#	1	BB_BA_27_HV_0215_SP		
#	2	BB_BA_27_HV_0115_SP		
#	3	BB_BA_27_HV_0315_SP		
#	4	BB_BA_27_HV_0615_SP		
#	5	BB_BA_27_HV_0415_SP
# PT Columns:		
#	0	TimeDate	
#	1	BB_BA_18_PT_0219	BB_BA_18_TT_0211	
#	3	BB_BA_18_PT_0119	BB_BA_18_TT_0111	
#	5	BB_BA_18_PT_0319	BB_BA_18_TT_0311	
#	7	BB_BA_18_PT_0619	BB_BA_18_TT_0611	
#	9	BB_BA_18_PT_0419	BB_BA_18_TT_0411	
#	11	BB_BA_27_PT_0215	BB_BA_27_TT_0213	
#	13	BB_BA_27_PT_0115	BB_BA_27_TT_0113	
#	15	BB_BA_27_PT_0315	BB_BA_27_TT_0313	
#	17	BB_BA_27_PT_0615	BB_BA_27_TT_0613	
#	19	BB_BA_27_PT_0415	BB_BA_27_TT_0413


fa00.write(f'{flowTitles[0]}\t{flowTitles[1]}\t{chokeTitles[1]}\t{ptTitles[1]}\t{ptTitles[2]}\n')	# B1-18-AE-0210 - F/C/P/T
fa02.write(f'{flowTitles[0]}\t{flowTitles[2]}\t{chokeTitles[2]}\t{ptTitles[3]}\t{ptTitles[4]}\n')	# B2-18-AE-0110 - F/C/P/T
fa05.write(f'{flowTitles[0]}\t{flowTitles[3]}\t{chokeTitles[3]}\t{ptTitles[15]}\t{ptTitles[16]}\n')	# B3-27-AE-0320 - F/C/P/T
fa06.write(f'{flowTitles[0]}\t{flowTitles[4]}\t{chokeTitles[4]}\t{ptTitles[7]}\t{ptTitles[8]}\n')	# B4-18-AE-0610 - F/C/P/T
fa08.write(f'{flowTitles[0]}\t{flowTitles[5]}\t{chokeTitles[5]}\t{ptTitles[9]}\t{ptTitles[10]}\n')	# B5-18-AE-0410 - F/C/P/T
#fa0.write(f'{flowTitles[0]}\t{flowTitles[]}\t{chokeTitles[]}\t{ptTitles[]}\t{ptTitles[]}\n')	# B1-18-AE-0210
fa01.write(f'{flowTitles[0]}\t{ptTitles[11]}\t{ptTitles[12]}\n')	# B1-27-AE-0220 -  / /P/T
fa03.write(f'{flowTitles[0]}\t{ptTitles[13]}\t{ptTitles[14]}\n')	# B2-27-AE-0120 -  / /P/T
fa07.write(f'{flowTitles[0]}\t{ptTitles[17]}\t{ptTitles[18]}\n')	# B4-27-AE-0620 -  / /P/T
fa09.write(f'{flowTitles[0]}\t{ptTitles[19]}\t{ptTitles[20]}\n')	# B5-27-AE-0420 -  / /P/T
fa10.write(f'{flowTitles[0]}\t{ptTitles[5]}\t{ptTitles[6]}\n')	# 18-AT-0310    -  / /P/T


for i in range(0, lines):
	fa00.write(f'{flowData[i][0]}\t{flowData[i][1]}\t{chokeData[i][1]}\t{ptData[i][1]}\t{ptData[i][2]}\n')	# B1-18-AE-0210 - F/C/P/T
	fa02.write(f'{flowData[i][0]}\t{flowData[i][2]}\t{chokeData[i][2]}\t{ptData[i][3]}\t{ptData[i][4]}\n')	# B2-18-AE-0110 - F/C/P/T
	fa05.write(f'{flowData[i][0]}\t{flowData[i][3]}\t{chokeData[i][3]}\t{ptData[i][15]}\t{ptData[i][16]}\n')	# B3-27-AE-0320 - F/C/P/T
	fa06.write(f'{flowData[i][0]}\t{flowData[i][4]}\t{chokeData[i][4]}\t{ptData[i][7]}\t{ptData[i][8]}\n')	# B4-18-AE-0610 - F/C/P/T
	fa08.write(f'{flowData[i][0]}\t{flowData[i][5]}\t{chokeData[i][5]}\t{ptData[i][9]}\t{ptData[i][10]}\n')	# B5-18-AE-0410 - F/C/P/T
	#fa0.write(f'{flowData[i][0]}\t{flowData[i][]}\t{chokeData[i][]}\t{ptData[i][]}\t{ptData[i][]}\n')	# B1-18-AE-0210
	fa01.write(f'{flowData[i][0]}\t{ptData[i][11]}\t{ptData[i][12]}\n')	# B1-27-AE-0220 -  / /P/T
	fa03.write(f'{flowData[i][0]}\t{ptData[i][13]}\t{ptData[i][14]}\n')	# B2-27-AE-0120 -  / /P/T
	fa07.write(f'{flowData[i][0]}\t{ptData[i][17]}\t{ptData[i][18]}\n')	# B4-27-AE-0620 -  / /P/T
	fa09.write(f'{flowData[i][0]}\t{ptData[i][19]}\t{ptData[i][20]}\n')	# B5-27-AE-0420 -  / /P/T
	fa10.write(f'{flowData[i][0]}\t{ptData[i][5]}\t{ptData[i][6]}\n')	# 18-AT-0310    -  / /P/T
	print(f'\rWriting Line {i} of {lines}\n')

fa00.close()
fa02.close()
fa05.close()
fa06.close()
fa08.close()

fa01.close()
fa03.close()
fa07.close()
fa09.close()
fa10.close()


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
