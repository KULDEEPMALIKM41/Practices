# Abstraction => it is an OOP feature which signify the hiding of background detail
#					and to give essential functionality to the user we use abstraction.
#				(this feature is use to implement application level security)
#			Note: in python abstraction is all about nomenclature (naming conventions)

# => Naming conventions for abstraction
# _____________________________________________________________________________________
# Naming conventions						significance				representation

# 									      inside   outside	other	
#									     class    class		class
# _____________________________________________________________________________________
# Data_member														    	 a
# Member_function	  public			  Y         Y         Y				 demoData	
# _____________________________________________________________________________________
# _datamember																_a
# _memberfunction     protected           Y         N         Y				_demoData
# _____________________________________________________________________________________
# __datamenber															   __a
# __memberfunction    privet			  Y			N		  N			   __demoData
# _____________________________________________________________________________________

#example public
class Demo:
	a=10
	def demoData(self):
		print('inside class  a= ',self.a)
obj=Demo()
obj.demoData()
print('outside class a=',obj.a)




#example protected
class Demo:
	_a=10
	def demoData(self):
		print('inside class  a= ',self._a)
obj=Demo()
obj.demoData()
print('outside class a=',obj._a)	# protected is only for say  




#example privet
class Demo:
	__a=10
	def demoData(self):
		print('inside class  a= ',self.__a)
obj=Demo()
obj.demoData()
#print('outside class a=',obj.__a)