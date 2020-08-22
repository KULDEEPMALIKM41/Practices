# 5.Hybrid inheritance =>

#									CLASS A(base class for B and C.)
#									   |
#						  _____________|________________
#					'is a'|								| 'is a'
#						  |								|
#	(derived class for A)CLASS B					CLASS C(derived class for A)
#	  (base class for D)  |						   	    |	(base class for D)
#						  |							    |
#						  _______________________________
#											|'is a'
#											|
#										  CLASS D(derived for B and C)

#Example:-

class A:
	def aData(self):
		print('class A member invoked')
				
class B(A):
	def bData(self):
		print('class B member invoked')
		
class C(A):
	def cData(self):
		print('class C member invoked')
		
class D(B,C):
	def dData(self):
		print('class D member invoked')
				
obj=D()
obj.aData()
obj.bData()
obj.cData()
obj.dData()
print('\n\n\n')



#Example:-

class A:
	def Data(self):
		print('class A member invoked')			
class B(A):
	def Data(self):
		super(B,self).Data()
		print('class B member invoked')
	
class C(A):
	def Data(self):
		super(C,self).Data()
		print('class C member invoked')
		
class D(B,C):
	def Data(self):
		super(D,self).Data()
		print('class D member invoked')
				
obj=D()
obj.Data()
print('\n\n\n')




#Example:-

class A:
	def Data(self):
		print('class A member invoked')			
class B(A):
	def Data(self):
		super(B,self).Data()
		print('class B member invoked')
	
class C(A):
	def Data(self):
		super(C,self).Data()
		print('class C member invoked')
		
class D(C,B):
	def Data(self):
		super(D,self).Data()
		print('class D member invoked')
				
obj=D()
obj.Data()
print('\n\n\n')




#Example:-

class A:
	def Data(self):
		print('class A member invoked')			
class B:
	def Data(self):
		super(B,self).Data()
		print('class B member invoked')
	
class C(A):
	def Data(self):
		super(C,self).Data()
		print('class C member invoked')
		
class D(C,B):
	def Data(self):
		super(D,self).Data()
		print('class D member invoked')
				
obj=D()
obj.Data()
print('\n\n\n')





#Example:-

class A:
	def Data(self):
		print('class A member invoked')			
class B(A):
	def Data(self):
		super(B,self).Data()
		print('class B member invoked')
	
class C:
	def Data(self):
		super(C,self).Data()
		print('class C member invoked')
		
class D(C,B):
	def Data(self):
		super(D,self).Data()
		print('class D member invoked')
				
obj=D()
obj.Data()
print('\n\n\n')



#Example:-

class A:
	def Data(self):
		print('class A member invoked')			
class B(A):
	def Data(self):
		super(B,self).Data()
		print('class B member invoked')
	
class C:
	def Data(self):
		super(C,self).Data()
		print('class C member invoked')
		
class D(B,C):
	def Data(self):
		super(D,self).Data()
		print('class D member invoked')
				
obj=D()
obj.Data()
print('\n\n\n')




#Example:-

class A:
	def Data(self):
		print('class A member invoked')			
class B(A):
	def Data(self):
		super(B,self).Data()
		print('class B member invoked')
	
class C(A):
	def Data(self):
		super(C,self).Data()
		print('class C member invoked')
		
class D(B,C):
	def dData(self):
		print('class D member invoked')
				
obj=D()
obj.Data()
obj.dData()
print('\n\n\n')



#Example:-

class A:
	def Data(self):
		print('class A member invoked')			
class B(A):
	def bData(self):
		print('class B member invoked')
	
class C(A):
	def Data(self):
		super(C,self).Data()
		print('class C member invoked')
		
class D(B,C):
	def dData(self):
		print('class D member invoked')
				
obj=D()
obj.Data()
obj.bData()
obj.dData()
print('\n\n\n')



#Example:-

class A:
	def Data(self):
		print('class A member invoked')			
class B(A):
	def bData(self):
		print('class B member invoked')
	
class C(A):
	def cData(self):
		super(C,self).Data()
		print('class C member invoked')
		
class D(B,C):
	def Data(self):
		print('class D member invoked')
				
obj=D()
obj.Data()
obj.bData()
obj.cData()
print('\n\n\n')