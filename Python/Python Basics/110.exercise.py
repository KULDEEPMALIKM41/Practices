# solution for constructor overriding.
class A:
	def __init__(self):
		print('class A constructor member called')
		
	def aData(self):
		print('class A member called')
		
class B(A):
	def __init__(self):
		super(B,self).__init__()
		print('class B constructor member called')
		
	def bData(self):
		print('class B member called')
		
obj=B()
obj.aData()
obj.bData()