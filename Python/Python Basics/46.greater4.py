#greater no. in fore values by if else.
a=int(input('Enter no. a \t'))
b=int(input('Enter no. b \t'))
c=int(input('Enter no. c \t'))
d=int(input('Enter no. d \t'))
if a>b and a>c and a>d:
	print('Greater No. is a')
if b>a and b>c and b>d:
	print('Greater No. is b')
if c>a and c>b and c>d:
	print('Greater No. is c')
if d>a and d>b and d>c:
	print('Greater No. is d')