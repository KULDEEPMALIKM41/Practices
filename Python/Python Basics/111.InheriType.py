#	Types of inheritance:-

# 1. Single Level Inheritance:-

#									CLASS A (base for B)
#									   |
#									   |
#									CLASS B	 (derived for A)

# Example:-
class Base: 
	'this is base class '
	a=10
	def baseData(self):
		print('this is base class method')
		
class Derived(Base):
	'this is derived class '
	b=20
	def derivedData(self):
		print('a : ',self.a)
		print('b : ',self.b)
		print('this is derived class method')

obj=Derived()
obj.baseData()
obj.derivedData()