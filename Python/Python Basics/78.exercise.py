
s='universal informatic'
s1='i'
print('element is found and index number is: ',s.find(s1,5))

#if element is not found in string by find function then this function is return -1.


s=input('enter string data : ')
s1=input('what is search : ')
w=int(input('where start searching from  : '))
s=s.find(s1,w)
if s==-1:
	print('element is not found')
else:
	print('element is found and index number is: ',s)



s=input('enter string data : ')
s1=input('what is search : ')
flage=0
for i in range(len(s)):
	if s[i]==s1:
		print('element is found and index number is : ',i)
		flage=1
if flage==0:
	print('element is not found')