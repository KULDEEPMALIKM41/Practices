#revers string by loop
s='universal'
print('your string is :',s)
print('your revers string is :',end='')
for i in range(len(s)-1,-1,-1):
	print(s[i],end='')
print('\n')
	
	
#revers string by range operator
s='universal'
print('your string is :',s)
print('your reverse string is :',s[::-1],'\n')
print('your reverse string is :',s[-1:-11:-1])