from lib.multhread import *
from lib.textnumbers import *
#Labels the joints for visual representation and user input
def labelization(image,cstats):
	graph = cstats[0]
	index = -1
	for node in graph:
		index+=1
		if index < 10:
			numline = getimgnum(index);
			#print(numline)
			for x in range(7):
				for y in range(7):
					image[node[0]+x-3][node[1]+y-3]=0
			for x in range(5):
				for y in range(5):
					image[node[0]+x-2][node[1]+y-2]=int(numline[y+(x*5)])*255
		else:
			indx = str(index)
			indx0 = int(indx[0])
			indx1 = int(indx[1])
			numline0 = getimgnum(indx0);
			numline1 = getimgnum(indx1);
			print(numline0)
			print(numline1)
			for x in range(7):
				for y in range(11):
					image[node[0]+x-3][node[1]+y-5]=0
			for x in range(5):
				for y in range(5):
					image[node[0]+x-2][node[1]+y-5]=int(numline0[y+(x*5)])*255
					image[node[0]+x-2][node[1]+y]=int(numline1[y+(x*5)])*255
	return image

#255 should be 1 while 0 should be 0/black
def getcolor(index):
	print(num)
	return 0
	
#Draws square joints onto the image
def jointization(cstats):
	graph = cstats[0]
	image = cstats[1]
	for node in graph:
		radius = lookup(node[2])
		for x in range(radius):
			for y in range(radius):
				image[node[0]+x-(radius/2)][node[1]+y-(radius/2)]=255
	print("Done")
	return image

#Calculates the average depth of color and generates a lowest sensitivity
def avgcolormain(current,sensitivity):
	coloraverage=0
	coloraverage = simulthread([avgcolor,len(current),coloraverage,current])
	coloraverage=coloraverage/len(current)
	coloraverage=coloraverage*sensitivity
	return coloraverage
	
#Finds clusters and sorts by largest clusters first. Reports center, and size of max allowed by settings
def clusterization(image,cluster_count):
	cstats=[]
	for x in range(len(image)):
		for y in range(len(image[0])):
			if image[x][y]==255:
				temp = centricate(x,y,image,1)
				image = temp[2]
				cstats.append([(temp[0]/(temp[3])),(temp[1]/(temp[3])),temp[3]])
	cstats = sorted(cstats, key=lambda x: x[2])
	cstats.reverse()
	print(cstats[:int(cluster_count)])
	return [cstats[:int(cluster_count)],image]
	
#recusrively finds and removes connecting joint points and counts them up. throws recursive errors on large joints given 
#python recursion limitations
def centricate(x,y,image,count):
	image[x][y]=0
	temp = []
	tx=0
	ty=0
	#print(str(count)+"x("+str(x)+","+str(y)+")")
	if image[x+1][y]==255:
		temp = centricate(x+1,y,image,count+1)
		tx+=temp[0]
		ty+=temp[1]
		image=temp[2]
		count=temp[3]
	if image[x-1][y]==255:
		temp = centricate(x-1,y,image,count+1)
		tx+=temp[0]
		ty+=temp[1]
		image=temp[2]
		count=temp[3]
	if image[x][y+1]==255:
		temp = centricate(x,y+1,image,count+1)
		tx+=temp[0]
		ty+=temp[1]
		image=temp[2]
		count=temp[3]
	if image[x][y-1]==255:
		temp = centricate(x,y-1,image,count+1)
		tx+=temp[0]
		ty+=temp[1]
		image=temp[2]
		count=temp[3]
		
	if image[x+1][y+1]==255:
		temp = centricate(x+1,y+1,image,count+1)
		tx+=temp[0]
		ty+=temp[1]
		image=temp[2]
		count=temp[3]
	if image[x-1][y+1]==255:
		temp = centricate(x-1,y+1,image,count+1)
		tx+=temp[0]
		ty+=temp[1]
		image=temp[2]
		count=temp[3]
	if image[x+1][y-1]==255:
		temp = centricate(x+1,y-1,image,count+1)
		tx+=temp[0]
		ty+=temp[1]
		image=temp[2]
		count=temp[3]
	if image[x-1][y-1]==255:
		temp = centricate(x-1,y-1,image,count+1)
		tx+=temp[0]
		ty+=temp[1]
		image=temp[2]
		count=temp[3]
	tx+=x
	ty+=y
	#print(str(x)+","+str(y))
	return [tx,ty,image,count]
	
def lookup(count):
	total = 0
	while (total*total)<count:
		total+=1
	if total < 13:
		total = 13
	return total