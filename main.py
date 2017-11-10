import cv2,sys
from lib.logging import *
from lib.multhread import *
from lib.imgproc import *

def main(img):
	settings = getSettings();
	print(settings)
	sys.setrecursionlimit(int(settings[2]))
	current = cv2.imread(img,0)
	coloraverage = avgcolormain(current,float(settings[0]))
	ender = [0]* len(current[0])
	ender = [ender]*len(current)
	simulthread([decolorize,len(current),ender,[current,coloraverage]])
	save(ender,'test')
	cstats = clusterization(ender,settings[1])
	save(cstats[1],'test2')
	jointed = jointization(cstats)
	save(jointed,'Base0')
	return

main('Base.jpg')