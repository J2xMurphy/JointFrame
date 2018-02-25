import math
#---------------------------------------------------------------------------
# This is used to calculate the angle using atan
def calcAngle(pt1,pt2,cstats,v):
	p1 = cstats[pt1]
	p2 = cstats[pt2]
## Reminder that P1 and P2 are formatted in Y: X: D: when output
	if v == 1:
		print(str(p1)+","+str(p2))
## sx is the x distance, while sy is the y distance
	sy = math.fabs(int(p2[0])-int(p1[0]))#---------------------------\
	sx = math.fabs(int(p2[1])-int(p1[1]))#                            \
	oy = int(p1[0])>int(p2[0])#                                                  \ Calculations for the ending tan
	ox = int(p1[1])>int(p2[1])#                                                  /---------------------------------  
	#if v == 1:
	#	tpx0=int(p1[0])-int(p2[0])
	#	print(str(p1[0])+",  "+str(p2[0])+",  "+str(tpx0))
	#	tpx1=int(p1[1])-int(p2[1])
	#	print(str(p1[1])+",  "+str(p2[1])+",  "+str(tpx1))
	sxy=round(float(sx/sy),2)#                                        /    
	#----------------------------------------------------------------/
	tsxy=math.atan(sxy)
	final = round(math.degrees(tsxy),2)
	verbose=0 
#---------------------------------------------------------------------------
#Depending on the quadrant, the final angle needs to be adjusted by 90x.
	if (oy==True and ox ==False):
		verbose = math.fabs(90-final)
		final = math.fabs(90-final)+90
	if (oy==False and ox ==False):
		verbose = final
		final = final
	if (oy==False and ox ==True):
		verbose = math.fabs(90-final)
		final = math.fabs(90-final)+270
	if (oy==True and ox ==True):
		verbose = final
		final = final+180
	if v == 1:	
		print("X:"+str(sx)+",   Y:"+str(sy)+",   tan("+str(sxy)+"), =  "+str(tsxy)+",   "+str(final)+",   "+str(verbose))
		print("oy:"+str(oy)+"   ox:"+str(ox))
	return final
#---------------------------------------------------------------------------
#										