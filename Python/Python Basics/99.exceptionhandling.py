#exception handling =>
#exception handling block =>

#				1. try - except

#				2. try - except - finally

#				3. try - finally

#				4. assert


#				1.try - except -->

#						syntax:-	try:
#										code block
#										excepted to raise error
#									except <Error_class_name>:
#										handling code

"""
print('before exception')
a=10
b=0
try:
	c=a/b
	print('result',c)
except ZeroDivisionError:
	print('Error: value of b must not be 0')
	b=int(input('enter b>0\n'))
	c=a/b
	print('result: ',c)
print('after exception')
print('\n\n\n')



print('before exception')

try:
	l=[10,20,30]
	print(l[0])
	
	d=10
	print('d=',d)
	
	a=10
	b=0
	c=a/b
	print('result :',c)
except NameError:
	print('Error: d is not define')
except ZeroDivisionError:
	print('value of b is must not be 0')
except Exception:
	print('Error')
print('after exception')
print('\n\n\n')


#				3. try - finally -->
#									this block is used to be implemented or priority
#							block that  is weather the exception is handle or not the 
#							finally block will be implemented or executed on finally block.


print('after exception:):):):):):):):):):):):):):):):)')
try:
	l=[10,20,30]
	print(l[5])
finally:
	print('before exception :):):):):):):):):):):):):)')
print('\n\n\n')


#				2. try - except - finally -->


print('before exception')

try:
	a=int(input('Enter a\n'))
	b=int(input('Enter b\n'))
	c=a/b
	print('result :',c)
	
	d=10
	print('d=',d)
	
	
	l=[10,20,30]
	print(l[10])
	
except ZeroDivisionError:
	print('Error: value of b must not be 0')
	b=int(input('Enter b > 0\n'))
	c=a/b
	print('result :',c)	

except NameError:
	print('Error: d is not define')
	
finally:	
	print('after exception')
	
	
"""				#4.Assert --> user define custom error
				
				
print('before execution')
a=int(input('Enter number a: '))
b=int(input('Enter number b: '))
assert(b!=0),'Error: b must not be 0'
c=a/b
print('result : ',c)
print('after exception')
