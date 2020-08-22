n=int(input('Enter any no.'))
c=0
while n!=0:
	b=n%10
	c=c*10
	c=c+b
	n=n//10
	
print('Reverse number is : ',c)