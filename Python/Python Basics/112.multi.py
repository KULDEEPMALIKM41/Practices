# 2.Multi Level Inheritance =>


#							CLASS A (base for B)
#							   |
#							   |
#							CLASS B (derived for A and base for C)
#							   |
#							   |
#							CLASS C (derived for B)

class A:
	def aData(self):
		print('class A member is invoked')
		
class B(A):
	def bData(self):
		print('class B member is invoked')
		
class C(B):
	def cData(self):
		print('class C member is invoked')
		
obj=C()
obj.aData()
obj.bData()
obj.cData()
print('\n\n\n')



# overriding solution in multi level inheritance:-

class A:
	def aData(self):
		print('class A member is invoked')
		
class B(A):
	def Data(self):
		print('class B member is invoked')
		
class C(B):
	def Data(self):
		super(C,self).Data()
		print('class C member is invoked')
		
obj=C()
obj.aData()
obj.Data()
print('\n\n\n')





class A:
	def Data(self):
		print('class A member is invoked')
		
class B(A):
	def Data(self):
		super(B,self).Data()
		print('class B member is invoked')
		
class C(B):
	def Data(self):
		super(C,self).Data()
		print('class C member is invoked')
		
obj=C()
obj.Data()