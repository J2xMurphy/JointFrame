import numpy as np
import cv2

def textexport(filename, image):
	f = open(filename, 'w')
	for i in range(len(image)):
		for j in range(len(image[i])):
			f.write(str(image[i][j]))
		f.write("\r\n")
	f.close()
	
def logexport(loglist):
	f = open("log.txt", 'w')
	f.write(loglist)
	f.close();
	
def save(nplist,outfile):
	nplist = np.asarray(nplist,dtype='float32')
	nplist = cv2.cvtColor(nplist,cv2.COLOR_GRAY2BGR)
	cv2.imwrite(outfile+'.jpg',nplist)
	print("Saved")
	
