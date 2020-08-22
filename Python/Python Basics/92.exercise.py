#fun prime or not prime
print('after execution')
def prime():
	'prime or not prime'
	a=int(input('enter any number'))
	flage=1
	for i in range(2,a):
		if a%i==0:
			flage=0
	if flage==1:
		print('prime')
	else:
		print('not prime')
prime()
			