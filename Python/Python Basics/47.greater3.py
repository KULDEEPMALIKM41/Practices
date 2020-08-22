# 1

a=int(input('Enter no. a \t'))
b=int(input('Enter no. b \t'))
c=int(input('Enter no. c \t'))
if a>b:
	if a>c:
		print('greater is a')
	else:
		print('greater is c')
else:
	if b>c:
		print('greater is b')
	else:
		print('greater is c')
		
		
# 2
		
a=int(input('Enter no. a \t'))
b=int(input('Enter no. b \t'))
c=int(input('Enter no. c \t'))
if a>b and a>c:
	print('Greater is a')
else:
	if b>c:
		print('Greater is b')
	else:
		print('Greater is c')
		
		
# 3. ladder if elif else

a=int(input('Enter no. a \t'))
b=int(input('Enter no. b \t'))
c=int(input('Enter no. c \t'))
if a>b and a>c:
	print('Greater is a')
elif b>c:
	print('Greater is b')
else:
	print('Greater is c')