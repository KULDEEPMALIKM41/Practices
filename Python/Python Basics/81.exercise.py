#searching with index number
l=[15,20,12,63,2,9,5,6,54]
flage=1
n=int(input('enter a number which you are searching - '))
for i in range(len(l)):
	if l[i]==n:
		flage=0
		print('element is found and index no. is - ',i)
if flage==1:
	print('element do not exist')
print()
print()

#reverse list
l=[1,2,3,4,9,6,8,7,5,0]
print("before reverse - ",l)
d=len(l)//2
for i in range(d):
	l[i],l[-(i+1)]=l[-(i+1)],l[i]
print('after reverse - ',l)
print()	
print()	


#descending order
l=[1,5,8,4,12,6,26.8,9,10]
print("list is - ",l)
for i in range(len(l)-1):
	for i in range(len(l)-1):
		if l[i]<l[i+1]:
			l[i],l[i+1]=l[i+1],l[i]
print("list descending order is - ",l)		





	
	