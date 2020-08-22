#add type 1

class Add:
	def addData(self):
		a=10				#local data member
		b=20
		c=a+b
		print('c= ',c)
		
	'''def showData(self):
		print('a=',a)		#error because a,b,c is not define.
		print('b=',b)
		print('c=',c)'''
obj=Add()
obj.addData()
#obj.showData()

print('\n\n\n')



#add type 2

class Add:
	a=10		#class level variable
	b=20
	def addData(self):

		self.c=self.a+self.b
		print('add = ',self.c)
		
	def showData(self):
		print('a=',self.a)		
		print('b=',self.b)
		print('c=',self.c)
obj=Add()		#when object is created then just value a,b is in existence.
obj.addData()
obj.showData()
print('\n\n\n')


#add type 3

class Add:
	def getData(self):
		self.a=10
		self.b=20
	def addData(self):
		self.c=self.a+self.b
	def showData(self):
		print('a: ',self.a)
		print('b: ',self.b)
		print('Add: ',self.c)
obj=Add()
obj.getData()
obj.addData()
obj.showData()