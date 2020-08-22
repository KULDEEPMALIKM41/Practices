#memory allocation
class Add:
	def getData(self,a,b):
		self.a=a
		self.b=b
	def addData(self):
		self.c=self.a+self.b
	def showData(self):
		print('a: ',self.a)
		print('b: ',self.b)
		print('Add: ',self.c)
obj=Add()
a=10
b=20
obj.getData(a,b)
obj.addData()
obj.showData()
print('\n\n\n')




class Employee:
	def getData(self):
		self.eno=input('Enter employee number \t')
		self.enm=input('Enter employee name \t')

	def showData(self):
		print('employee detail')
		print('Empolyee number: ',self.eno)
		print('Employee name: ',self.enm)
obj=Employee()
obj.getData()
obj.getData()
obj.getData() #last input replace first two input.
obj.showData()
obj.showData()
obj.showData()
print('\n\n\n')



class Employee:
	def getData(self):
		self.eno=input('Enter employee number \t')
		self.enm=input('Enter employee name \t')

	def showData(self):
		print('employee detail')
		print('Empolyee number: ',self.eno)
		print('Employee name: ',self.enm)
obj=Employee()
obj1=Employee()
obj2=Employee()
obj.getData()
obj1.getData()
obj2.getData()
obj.showData()
obj1.showData()
obj2.showData()
print('\n\n\n')




class Employee:
	def getData(self):
		self.eno=input('Enter employee number \t')
		self.enm=input('Enter employee name \t')

	def showData(self):
		print('employee detail')
		print('Empolyee number: ',self.eno)
		print('Employee name: ',self.enm)
emp=[]
n=int(input('Number of employee : '))
for i in range(n):
	emp.append(Employee())
print('Enter employee detail')
for i in range(n):
	emp[i].getData()
for i in range(n):
	emp[i].showData()
print('\n\n\n')





class Employee:
	emp=[]
	def employeeGetdata(self):
		n=int(input('Number of employee : '))
		for i in range(n):
			self.emp.append({})
		
		for d in self.emp:
			print('Enter employee detail')
			k=input('enter key name : ')
			d[k]=input('Enter value \t')
			k=input('enter key name : ')
			d[k]=input('Enter value \t')
			print('\n')
	def employeeShowdata(self):
		for d in self.emp:
			print(' employee detail')
			for key in d:
				print(key,' : ',d[key])
			print('\n')
obj=Employee()
obj.employeeGetdata()
obj.employeeShowdata()
		

