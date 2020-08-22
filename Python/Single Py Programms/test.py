#Example:-
class a:
	def Data(self):
		print('class a member invoked')

class A(a):
	def Data(self):
		super(A,self).Data()
		print('class A member invoked')
				
class B(a):
	def Data(self):
		super(B,self).Data()
		print('class B member invoked')
		
class C(A,B):	# first class member function is call which same name.
	def Data(self): 
		super(C,self).Data()
		print('class C member invoked')
				
obj=C()
obj.Data()
print('\n\n\n')




class A:
	def Data(self):
		super(A,self).Data()
		print('class A member invoked')
				
class B:
	def Data(self):
		print('class B member invoked')
		
class C(A,B):	# first class member function is call which same name.
	def Data(self): 
		super(C,self).Data()
		print('class C member invoked')

obj=C()

obj.Data()
				
