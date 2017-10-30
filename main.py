import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
import scipy.ndimage as sp
import copy
import thread
import time
global loglist
loglist=""

def main(img):
	global current
	global coloraverage
	coloraverage=0
	current = cv2.imread(img,0)
	cuslog(str(len(current[0]))+","+str(len(current)))
	cuslog(current[0][0])
	cuslog(len(current))
	simulthread(avgcolor);
	coloraverage=coloraverage/len(current)
	coloraverage=coloraverage*.5
	cuslog(str(coloraverage))
	simulthread(decolorize);
	return

def cuslog(string):
	global loglist
	loglist+=str(string)
	loglist+="\n"
	
def simulthread(function):
	global current
	global threads
	threads = len(current);
	i=0
	for i in range(len(current)):
		thread.start_new_thread ( function, (i,) )
	cuslog("Created all threads");
	while (threads > 1):
		cuslog(str(threads)+" threads remaining.")
		time.sleep(.1)
	cuslog(str(threads)+" threads remaining.")
	
def avgcolor(line):
	global coloraverage
	totalcolor=0
	global current
	global threads
	for j in range(len(current[line])):
		totalcolor+=current[line][j]
	threads-=1
	coloraverage+=(totalcolor/j)
	thread.exit()
	
def save(nplist,outfile):
	nplist = np.asarray(nplist,dtype='float32')
	nplist = cv2.cvtColor(nplist,cv2.COLOR_GRAY2BGR)
	cv2.imwrite(outfile+'.jpg',nplist)
	print("Saved")
	
def decolorize(line):
	global coloraverage
	j=0
	global current
	global threads
	for j in range(len(current[line])):
		if current[line][j]>=coloraverage:
			current[line][j]=0
		else:
			current[line][j]=255
	threads-=1
	thread.exit()
	
def textexport(filename, image):
	f = open(filename, 'w')
	for i in range(len(image)):
		for j in range(len(image[i])):
			f.write(str(image[i][j]))
		f.write("\r\n")
	f.close()
	
def logexport():
	global loglist
	f = open("log.txt", 'w')
	f.write(loglist)
	f.close();

global current
cuslog("Beginning Translation")
main('Base.jpg')
cuslog("Ending Translation")
cuslog(current[0][0])
save(current,'test')
logexport();
#textexport('workfile',current)