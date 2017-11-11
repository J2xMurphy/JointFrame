import numpy as np
import cv2
#Dont think anything here is useful
#Exports an image into a text file
def textexport(filename, image):
	f = open(filename, 'w')
	for i in range(len(image)):
		for j in range(len(image[i])):
			f.write(str(image[i][j]))
		f.write("\r\n")
	f.close()
#Currently unused, exports a string to a txt	
def logexport(loglist):
	f = open("log.txt", 'w')
	f.write(loglist)
	f.close();
#saves a given image by a given name
def save(nplist,outfile):
	nplist = np.asarray(nplist,dtype='float32')
	nplist = cv2.cvtColor(nplist,cv2.COLOR_GRAY2BGR)
	cv2.imwrite(outfile+'.jpg',nplist)
	print("Saved")
#opens settings, honestly should use for generic files but whatever.
def getSettings():
	f = open('Settings.txt','r')
	cont = True
	settings=[]
	while cont==True:
		temp = f.readline()
		if temp != '':
			temp = temp.replace("\r\n","")
			settings.append(temp)
		else:
			cont=False
	return settings