# 4. multiple inheritance =>


#           (base for C)CLASS A          					CLASS B(base for C)
#						  |									   |
#						  |									   |
#						  ______________________________________
#											|
#											|
#										  CLASS C(derived for A and B)

# Drawback of other technology =>

#		1.if base class will contain functionality with same name it may
#			generate ambiguity problem.

#		2. their is no possibility to extends(inherit) multiple class
#			simultaneously.


#Example:-

class A:
	def aData(self):
		print('class A member invoked')
				
class B:
	def bData(self):
		print('class B member invoked')
		
class C(A,B):
	def cData(self):
		print('class C member invoked')
				
obj=C()
obj.aData()
obj.bData()
obj.cData()
print('\n\n\n')

#Example:-

class A:
	def Data(self):
		print('class A member invoked')
				
class B:
	def Data(self):
		print('class B member invoked')
		
class C(A,B):	# first class member function is call which same name.
	def cData(self):
		print('class C member invoked')
				
obj=C()
obj.Data()
obj.cData()
print('\n\n\n')


#Example:-

class A:
	def Data(self):
		print('class A member invoked')
				
class B:
	def Data(self):
		print('class B member invoked')
		
class C(B,A):	# first class member function is call which same name.
	def cData(self):
		print('class C member invoked')
				
obj=C()
obj.Data()
obj.cData()
print('\n\n\n')



#Example:-

class A:
	def Data(self):
		print('class A member invoked')
				
class B:
	def Data(self):
		print('class B member invoked')
		
class C(B,A):	# first class member function is call which same name.
	def Data(self): 
		super(C,self).Data()
		print('class C member invoked')
				
obj=C()
obj.Data()
print('\n\n\n')




#Example:-

class A:
	def Data(self):
		print('class A member invoked')
				
class B:
	def bData(self):
		print('class B member invoked')
		
class C(A,B):	# first class member function is call which same name.
	def Data(self): 
		super(C,self).Data()
		print('class C member invoked')
				
obj=C()
obj.bData()
obj.Data()
print('\n\n\n')






#Example:-

class A:
	def aData(self):
		print('class A member invoked')
				
class B:
	def Data(self):
		print('class B member invoked')
		
class C(A,B):	# first class member function is call which same name.
	def Data(self): 
		super(C,self).Data()
		print('class C member invoked')
				
obj=C()
obj.aData()
obj.Data()
print('\n\n\n')