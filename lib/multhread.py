import thread
import time
# Use as a list of args, 0:function, 1:range 2:return, 3: custom
def simulthread(args):
	threads=[]
	function=args[0]
	threads = [0]
	for i in range(args[1]):
		threads[0]+=1
		thread.start_new_thread ( function, ([i]+[threads]+[args],))#args becom 0:thread no, 1[0:thread amt]
																	#,2[0:function, 1:range 2:return, 3: custom]
	print("Created all threads");
	while (threads[0] > 0):
		print(str(threads[0])+" threads remaining.")
		time.sleep(.1)
	print(str(threads)+" threads remaining!")
	return args[2]

	
def avgcolor(args):
	totalcolor=0
	current=args[2][3][(args[0])]
	for j in range(len(current)):
		totalcolor+=current[j]
	args[1][0]-=1
	args[2][2]+=(totalcolor/j)
	thread.exit()
	
def decolorize(args):
	coloraverage = args[2][3][1]
	current=args[2][3][0][args[0]]
	for j in range(len(current)):
		if current[j]>=coloraverage:
			current[j]=0
		else:
			current[j]=255
	args[2][2][args[0]]=current
	args[1][0]-=1
	thread.exit()