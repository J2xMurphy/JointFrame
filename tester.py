import cv2
import sys
from lib.logging import *
from lib.c8 import *
#This is a test version of the angle calculator
def begintests(testname,settings):
#---------------------------------------------------------------------------
# These are the usable values in cstats.jt
	f = open(testname+".jt","r")
	cstats = f.readline()
	cstats = tupStringtoIntList(cstats)
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# These are the usable values in connections.txt
	g = getStrings(testname+".test")
	newstrings = []
	for item in g:
		newstrings.append(tupStringtoIntTup(item))
#---------------------------------------------------------------------------
	angles = []
	for item in newstrings:
		angles.append(round(calcAngle(item[0],item[1],cstats,settings[0]),2))
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
# Comparing derived answers to given solutions
	#print(angles)
	solutions = getStrings(testname+".sol")
	i = 0
	correct=0
	total=0
	print("\n")
	for ans in solutions:
		#currenttest=(round(angles[i],2)<=round(float(ans),2)+.1 and round(angles[i],2)<=round(float(ans),2)-.1)
		currenttest = round(float(ans),2)-.1<=round(angles[i],2)<=round(float(ans),2)+.1
		correct+=currenttest
		total+=1
		print("Test "+str(i)+": ["+str(angles[i])+" : "+ans+"]  "+str(currenttest==1))
		i+=1
	print(str(correct)+"/"+str(total))
#---------------------------------------------------------------------------
settings = [0]
for arg in sys.argv:
	if arg == 'v':
		settings[0]=1
begintests("tests/connections1",settings)
begintests("tests/connections2",settings)
begintests("tests/connections3",settings)
begintests("tests/connections4",settings)
begintests("tests/connections5",settings)
begintests("tests/connections6",settings)