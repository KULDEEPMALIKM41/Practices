# Method overriding in inheritance:-
#								in case of inheritance when one class acquires
#				the property of another class and the property of will be same
#				name the derived class will override the property of base class
#				it is method overloading.

# Example:- 
class A:
	def Data(self):
		print('class A member called')
		
class B(A):
	def Data(self):
		print('class B member called')
		
obj=B()
obj.Data()
print('\n\n\n')

#solution:-
class A:
	def Data(self):
		print('class A member called')
		
class B(A):
	def Data(self):
		super(B,self).Data()
		print('class B member called')

obj=B()
obj.Data()