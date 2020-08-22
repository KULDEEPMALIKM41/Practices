# 3.Hierarchical Inheritance =>

#									CLASS A(base class for B and C.)
#									   |
#						  _____________|________________
#					is a  |								| is a
#						  |								|
#	(derived class for A)CLASS B					CLASS C(derived class for A)

#Example:-
class A:
	def aData(self):
		print('class A member is invoked')
		
class B(A):
	def bData(self):
		print('class B member is invoked')
		
class C(A):
	def cData(self):
		print('class C member is invoked')

obj1=B()
obj1.aData()
obj1.bData()		
obj2=C()
obj2.aData()
obj2.cData()

print('\n\n\n')


#overriding solution:-
class A:
	def Data(self):
		print('class A member is invoked')
		
class B(A):
	def bData(self):
		print('class B member is invoked')
		
class C(A):
	def Data(self):
		super(C,self).Data()
		print('class C member is invoked')

obj1=B()
obj1.Data()
obj1.bData()		
obj2=C()
obj2.Data()