# Inheritance => inheritance is an object oriented feature use to implement code
# 				reusability and modularity in an application.

#	NOTE:- inheritance also called "is a" relationship.

#	it is an concept with signify sharing of property of one class in another class.

#				CLASS A ---------------------> CLASS B
#  base\parent\super class for CLASS B    derived\child\sub class for CLASS A
		
# Syntax:-		class Base:
#					'base class doc string'
#					base class suite
#				class Derived(Base):
#					'derived class doc string'
#					derived class suite

# Example:-
class Base:
	'this is base class'
	def baseData(self):
		print('this is base class method')
		
class Derived(Base):
	'this is derived class'
	def derivedData(self):
		print('this is derived class method')
		
obj=Derived()
obj.baseData()
obj.derivedData()
print('\n\n\n')

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























