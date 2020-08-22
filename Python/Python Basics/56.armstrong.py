n=int(input('enter any number'))
c=0
a=n
while n!=0:
	b=n%10
	c=c+b**3
	n=n//10
if a==c:
	print('armstrong')
else:
	print('not armstrong')