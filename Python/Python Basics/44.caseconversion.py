#Case conversion

s=input('Enter any type of charactor \t')
if ord(s)>=65 and ord(s)<=90:
	c=ord(s)
	print('lower case is : ',chr(c+32))
if ord(s)>=97 and ord(s)<=122:
	c=ord(s)
	print('upper case is : ',chr(c-32))