rows = 10
cols = 27
import time
for i in range(1,rows):
	for j in range(i,cols):
		print(' ',end='',flush=True)
	for k in range(1,i+1):
		print(' *',end='',flush=True)
	time.sleep(0.2)
	print()
for i in range(1,rows):
	for j in range(1,i+1):
		print(' ',end='',flush=True)
	for k in range(i,cols):
		print(' *',end='',flush=True)
	time.sleep(0.2)
	print()