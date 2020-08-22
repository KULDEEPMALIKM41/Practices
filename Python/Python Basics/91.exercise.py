#fun factorial
print('before execution')
def factorial():
	'factorial'
	a=int(input('enter any number'))
	b=a
	for i in range(1,a):
		b=b*i
	print('factorial is: ',b)
factorial()
print('after execution')
		