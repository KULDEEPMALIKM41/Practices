# destructor => 

#		1. it is member method of class.

#		2. it is used to delete the member of an class.

#		3. their is no need to call destructor functionality, it will be auto
#		   called at thee last of program execution.

#		4. In python destructor will have fixed name.

#									def __del__(self):
#											statement

#		5. special member method.

#example:-

class Employee:
	def __init__(self):
		print('constructor has invoked')
		self.eno=None
		self.enm=None
		
	def getEmployee(self):
		self.eno=1001
		self.enm='kuldeep'
		
	def showEmployee(self):
		print('eno : ',self.eno)
		print('enm : ',self.enm)
		
	def __del__(self):
		pass
		
obj=Employee()
obj.showEmployee()
obj.getEmployee()
obj.showEmployee()	