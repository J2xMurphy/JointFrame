from lib.multhread import *
#Calculates the average depth of color and generates a lowest sensitivity
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

def avgcolormain(current,sensitivity):
	coloraverage=0
	coloraverage = simulthread([avgcolor,len(current),coloraverage,current])
	coloraverage=coloraverage/len(current)
	coloraverage=coloraverage*sensitivity
	return coloraverage
	
def clusterization(image,cluster_count):
	cstats=[]
	for x in range(len(image)):
		for y in range(len(image[0])):
			if image[x][y]==255:
				temp = centricate(x,y,image,1)
				image = temp[2]
				cstats.append([(temp[0]/(temp[3])),(temp[1]/(temp[3])),temp[3]])
	#print(cstats)
	cstats = sorted(cstats, key=lambda x: x[2])
	#print(cstats)
	cstats.reverse()
	#print(cstats)
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
	if total < 7:
		total = 7
	return total