import cv2,sys
from lib.logging import *
from lib.multhread import *
from lib.imgproc import *

def main(img):
	settings = getStrings('Settings.txt');
	print(settings)
	sys.setrecursionlimit(int(settings[2]))
	current = cv2.imread(img,0)
	coloraverage = avgcolormain(current,float(settings[0]))
	ender = [0]* len(current[0])
	ender = [ender]*len(current)
	simulthread([decolorize,len(current),ender,[current,coloraverage]])
	save(ender,'Base0')
	cstats = clusterization(ender,settings[1])
	#save(cstats[1],'test2')
	logexport(str(cstats[0]),"cstats.jt")
	jointed = jointization(cstats)
	save(jointed,'Base1')
	labeled = labelization(jointed,cstats)
	save(labeled,'Base2')
	return

main('Base.jpg')