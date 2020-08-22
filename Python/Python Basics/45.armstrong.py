n=int(input('Enter any number'))
a=(n)%10
b=n//10
b=b%10
c=n//100
if n==a**3+b**3+c**3:
	print('armstrong')
else:
	print(' not armstrong')
	




	
n=input('Enter any number')

a=int(n[2])
b=int(n[1])
c=int(n[0])
if int(n)==a**3+b**3+c**3:
	print('armstrong')
else:
	print(' not armstrong')