import cv2
from lib.logging import *
from lib.c8 import *
#The second will be rotated to attatch to the first
def main():
#---------------------------------------------------------------------------
# These are the usable values in cstats.jt
	f = open("cstats.jt","r")
	cstats = f.readline()
	cstats = tupStringtoIntList(cstats)
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# These are the usable values in connections.txt
	g = getStrings('connections.txt')
	newstrings = []
	for item in g:
		newstrings.append(tupStringtoIntTup(item))
#---------------------------------------------------------------------------
	angles = []
	fs =""
	for item in newstrings:
		tmp = calcAngle(item[0],item[1],cstats)
		angles.append(tmp)
		fs+=("("+str(item[0])+","+str(item[1])+") : "+str(tmp)+"\r\n")
	print(angles)
	logexport(fs,"angles.txt")
main()