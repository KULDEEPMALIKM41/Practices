# pelendro number

n=int(input('enter any 3 digit number \n'))
b=n%10
c=n//100
if (b==c):
	print('number is pelindro')
if (b!=c):
	print('number is normal')