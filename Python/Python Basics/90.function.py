#function => function are block of code which is created as user requirement this code
#			of block will be invoked when called.

#			two types of function=> 1. predefine 		2.user define

#					2.user define =>
#
#						syntax:- def function_name(argument if any)
#										'function doc. string(optional)' 
#										 statement
#										 return value(if any)
#
#						calling syntax:-  function_name()


#bug
#demo()   #error : demo is not define
print('before execution')
def demo():
	'this is my first function'   #in function it's function information(meta information)
	print('this is demo function invoked')
demo()
print('after execution')



print('before execution')
def demo():
	'this is my first function'   #in function it's function information(meta information)
	print('this is demo function invoked')
demo()
print('after execution')