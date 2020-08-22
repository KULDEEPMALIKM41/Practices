class Employee:
	eno=None	#class level variable declaration work same as constructor
	enm=None	# but not a constructor because when it's class's object is 
				# created then this variable is in auto existence.
	def getEmployee(self):
		self.eno=1001
		self.enm='kuldeep'
		
	def showEmployee(self):
		print('Eno : ',self.eno)
		print('Enm : ',self.enm)
		
		
obj=Employee()
#obj.getEmployee()
obj.showEmployee()