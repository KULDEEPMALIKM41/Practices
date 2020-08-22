# excercise 1 

class Employee:

	increment = 1.5 #class level variables
	no_of_employees = 0
	def __init__(self, fname, lname, salary):
		self.fname = fname					# object or instance variables
		self.lname = lname
		self.salary = salary
		Employee.no_of_employees += 1

	def increse(self):
		self.salary = int(self.salary*self.increment)

	''' @classmethod will allow us to call that method using the class name instead of the object.
		this method use for make class level changes and take by default one argument(class).
	'''
	@classmethod
	def change_increment(cls, amount):
		cls.increment = amount

	@classmethod
	def from_str(cls, emp_string):
		fname, lname, salary = emp_string.split('-')
		return cls(fname, lname, salary)

	''' @staticmethod will allow us to call that method using the class name or an instance of a class.
		this method use for make class level changes and take by default zero argument.
	'''
	@staticmethod
	def isopen(day):
		if day.lower() == "sunday":
			return False
		else:
			return True

# print(Employee.isopen('Monday'))

# kuldeep = Employee('kuldeep','mali',50000)
# lovish = Employee.from_str("lovish-jecson-5000")
# sanjay = Employee('sanjay','singh',1000)

# print(kuldeep.__dict__) # object or instance variables
# print(Employee.__dict__) #class level variables

# print(lovish.salary)
# print(kuldeep.salary)

# print(Employee.increment)
# Employee.change_increment(4)
# print(Employee.increment)

# kuldeep.increse()
# print(kuldeep.salary)


# excercise 2
class Student:
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
		self._email = self.fname + self.lname + "@gmail.com"

	@property 		# @property decorater use for get value.
	def email(self):
		return self._email

	@email.setter	# @email.setter decorater use for set value.
	def email(self, given_mail):
		self._email = given_mail

	@email.deleter	# @email.deleter decorater use for delete value.
	def email(self):
		self._email = None

kuldeep = Student('kuldeep','mali')
print(kuldeep.fname)

print(kuldeep.email) # call @property email

kuldeep.lname = "malik"
print(kuldeep.email) # call @property email

kuldeep.email = "malikuldeep@gmail.com"    # call @email.setter email
print(kuldeep.email) # call @property email

del kuldeep.email 	 # call @email.deleter email
print(kuldeep.email) # call @property email



# excercise 3
class Programer:
	def __init__(self, fname, lname, salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary

	def __add__(self,other):
		return self.salary + other.salary

	def __repr__(self): # we can use __str__ method also. Both are same.
		return self.fname +' '+ self.lname

# kuldeep = Programer('kuldeep','mali',556535)
# sanjay = Programer('sanjay','singh',65456)

# print(4+5)
# print('4'+'5')

# a=6
# print(a.__add__(5))
# print(a.__mul__(5))

# print(kuldeep+sanjay)

# print(kuldeep)