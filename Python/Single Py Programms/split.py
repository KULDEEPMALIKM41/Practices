for i in range(1,6):
	for j in range(i,6):
		print("",end="")
	if i==1:
		print('1')
	else:
		for k in range (1,i+2):
			if k==1:
				print('1 ',end='')
			elif k==(i+1):
				print('1 ',end='')
			elif i==4 and k==3:
				print('6 ',end='')
			elif i==5 and (k==3 or k==4):
				print('10 ',end='')
			else:
				print(i," ",end="")
		print()

