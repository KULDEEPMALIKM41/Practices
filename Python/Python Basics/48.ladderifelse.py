a=int(input('Enter no. a \t'))
b=int(input('Enter no. b \t'))
c=int(input('Enter no. c \t'))
d=int(input('Enter no. d \t'))
if a>b and a>c and a>d:
	print('greater is a')
else:
	if b>c and b>d:
		print('Greater is b')
	else:
		if c>d:
			print('greater is c')
		else:
			print('greater is d')

			
			
#nested if else is update in ladder if-elif-else.

a=int(input('Enter no. a \t'))
b=int(input('Enter no. b \t'))
c=int(input('Enter no. c \t'))
d=int(input('Enter no. d \t'))
if a>b and a>c and a>d:
 print('greater is a')
elif b>c and b>d:
 print('Greater is b')
elif c>d:
	print('greater is c')
else:
 print('greater is d')

