import cv2
from lib.logging import *
from lib.multhread import *
from lib.imgproc import *

def main(img):
	current = cv2.imread(img,0)
	coloraverage = avgcolormain(current)
	ender = [0]* len(current[0])
	ender = [ender]*len(current)
	simulthread([decolorize,len(current),ender,[current,coloraverage]])
	save(ender,'test')
	return

main('Base.jpg')