#classification of user define function base of return  value and argument.
# 1. function without return type & without argument.

def demo():
	print('without argument and witout return type')
	print('inside function a=',a,'b=',b)
a=10
b=20
demo()
print('outside function a=',a,'b=',b,'\n\n')





# 2. function without return type and with argument.

def demo(x,y):			#formal parameter.
	print('with argument and without return type')
	print('inside function a=',x,'b=',y)
a=10
b=20
demo(a,b)				#actual parameter.
print('outside function a=',a,'b=',b,'\n\n')




# 3. function with return type and without argument.


def demo():
	a=10				#local parameter is not access in global scope.
	b=20
	print('without argument and with return type')
	print('inside function c=',a+b)
	return(a+b)

c=demo()
print('outside function c=',c,'\n\n')



# 4. function with return type and with argument.


def demo(x,y):
	'function with return type and with argument'
	print("inside finction : ",x+y)
	return(x+y)
a=10
b=20
c=demo(a,b)
print("outside the function : ",c)









