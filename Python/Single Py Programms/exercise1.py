for i in range(1,9):
	if i%2==1:
		for j in range(1,10-i):
			print(j,end=' ')
		print()
	else:
		for j in range(9-i,0,-1):
			print(j,end=' ')
		print()
	