from lib.multhread import *
def avgcolormain(current):
	coloraverage=0
	coloraverage = simulthread([avgcolor,len(current),coloraverage,current])
	coloraverage=coloraverage/len(current)
	f = open('Settings.txt','r')
	sensitivity = float(f.readline())
	coloraverage=coloraverage*sensitivity
	return coloraverage