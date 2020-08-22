#first 20 febonasi series. 
a=-1
b=1
i=1
while i<=10:
	a=a+b
	b=a+b
	i+=1
	print(a,end=' ')
	print(b,end=' ')
print()
	
	
#first 20 febonasi series.	
a,b,i=-1,1,1
while i<=20:
	c=a+b
	print(c,end=' ')
	a=b
	b=c         #a,b=b,c
	i+=1