n=int(input('enter any number'))
temp=n
rev=0
while n!=0:
	a=n%10
	rev=rev*10+a
	n=n//10
if temp==rev:
	print('number is pelindroms')
else:
	print('number is normal')