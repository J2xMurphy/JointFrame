import numpy as np
import cv2
import re
#Dont think anything here is too useful
#Converts a list string to a list
def tupStringtoIntList(strlist):
	strlist = re.sub('\[',"",re.sub('\],',"]",re.sub(' ',"",strlist)))
	newlists=[]
	curstring=""
	for letters in strlist:
		if letters != "]":
			curstring+=letters
		else:
			print(curstring)
			newlists.append(curstring)
			curstring=""
	actlists=[]
	for i in range(len(newlists)-1):
		actlists.append(newlists[i].split(","))
	return actlists

#Converts a tuple string to two a int tuple
def tupStringtoIntTup(strtuple):
	strtuple = re.sub('\)',"",re.sub('\(',"",strtuple))
	strtuple = strtuple.split(",")
	return (int(strtuple[0]),int(strtuple[1]))
	
#Exports an image into a text file
def textexport(filename, image):
	f = open(filename, 'w')
	for i in range(len(image)):
		for j in range(len(image[i])):
			f.write(str(image[i][j]))
		f.write("\r\n")
	f.close()
#Currently unused, exports a string to a txt	
def logexport(loglist,name):
	f = open(name, 'w')
	f.write(loglist)
	f.close();
#saves a given image by a given name
def save(nplist,outfile):
	nplist = np.asarray(nplist,dtype='float32')
	nplist = cv2.cvtColor(nplist,cv2.COLOR_GRAY2BGR)
	cv2.imwrite(outfile+'.jpg',nplist)
	print("Saved")
#opens settings, honestly should use for generic files but whatever.
def getStrings(name):
	f = open(name,'r')
	cont = True
	names=[]
	while cont==True:
		temp = f.readline()
		if temp != '':
			temp = temp.replace("\r\n","")
			names.append(temp)
		else:
			cont=False
	return names