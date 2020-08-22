import time
stime=time.time()
print('before execution')
a=5
for i in range(1,11):
	c=a*i
	print('table is : ',c)
	#time.sleep(1)			#1second time delay for loop per execution.
print('after execution')
etime=time.time()
time_delay=etime-stime
print('total execution time : ',time_delay)