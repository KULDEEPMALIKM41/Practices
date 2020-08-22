n=int(input('enter any no'))
i=2
while i<=(n/2):
	if n%i==0:
		print('not prime')
		break
	if i==int(n/2):
		print('prime')
	i=i+1
	

	
n=int(input('enter any no'))
flag=1
i=2
while i<n:
	if n%i==0:
		flag=0
	i=i+1
if flag==0:
	print('not prime')
else:
	print('prime')
