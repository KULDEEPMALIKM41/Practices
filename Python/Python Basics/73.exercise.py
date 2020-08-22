for i in range(1,9):
	if i%2!=0:
		for j in range (8,-1+i,-1):
			print(j,end=" ")
		
	else:
		for j in range(i,9):
			print(j,end=" ")
	print()
	
