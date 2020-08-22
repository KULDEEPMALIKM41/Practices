#protected
class A:
	'class A doc string'
	_a=100
	def aData(self):
		print('class A member called')
		
class B(A):
	'class B doc string'
	_b=200
	def bData(self):
		print('a : ',self._a)			#access in another class.
		print('b : ',self._b)
		print('class B member called')
		
obj=B()
obj.aData()
obj.bData()
#print('a outside of class : ',obj.a)   # not access outside of class.
print('\n\n\n')




#privet
class A:
	'class A doc string'
	__a=100
	def aData(self):
		print('class A member called')
		
class B(A):
	'class B doc string'
	__b=200
	def bData(self):
#		print('a : ',self.__a)  # not access in another class.
		print('b : ',self.__b)
		print('class B member called')
		
obj=B()
obj.aData()
obj.bData()
#print('a outside of class : ',obj.__a) # not access outside of class.