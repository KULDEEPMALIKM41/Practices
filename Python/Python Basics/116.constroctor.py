# Constructor => 

#		1. it is member method of class.

#		2. it is used to initialize the member of an class with default value.

#		3. their is no need to call constructor functionality, it will be auto
#		   called when object of class is created.

#		4. In python constructor will have fixed name.

#									def __init__(self):
#											statement

#		5. special member method.

# Types of constructor :-
#		1. O-parameterized or default Constructor.

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
		
obj=Employee()
obj.showEmployee()
obj.getEmployee()
obj.showEmployee()		
	

	
#		2.parameterized Constructor.


class Employee:
	def __init__(self,eno,enm):
		print('constructor has invoked')
		self.eno=eno
		self.enm=enm
		
	def getEmployee(self):
		self.eno=1001
		self.enm='kuldeep'
		
	def showEmployee(self):
		print('eno : ',self.eno)
		print('enm : ',self.enm)
		
obj=Employee(0,'Null')
#obj1=Employee()			#type Error, required 2 parameter.
obj.showEmployee()
obj.getEmployee()
obj.showEmployee()