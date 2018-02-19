import math
#---------------------------------------------------------------------------
# This is used to calculate the angle using atan
def calcAngle(pt1,pt2,cstats):
	p1 = cstats[pt1]
	p2 = cstats[pt2]
## Reminder that P1 and P2 are formatted in Y: X: D: when output
	print(str(p1)+","+str(p2))
## sx is the x distance, while sy is the y distance
	sy = math.fabs(int(p2[0])-int(p1[0]))#---------------------------\
	sx = math.fabs(int(p2[1])-int(p1[1]))#                            \
	ox = p1[0]>p2[0]#                                                  \ Calculations for the ending tan
	oy = p1[1]>p2[1]#                                                  /---------------------------------     
	sxy=round(float(sx/sy),2)#                                                 /    
	#----------------------------------------------------------------/
	tsxy=math.atan(sxy)
	print("X:"+str(sx)+",   Y:"+str(sy)+",   tan("+str(sxy)+"), =  "+str(tsxy)+",   "+str(math.degrees(tsxy)))
	print("ox:"+str(ox)+"   oy:"+str(oy))
	return round(math.degrees(tsxy),2)
#---------------------------------------------------------------------------
#