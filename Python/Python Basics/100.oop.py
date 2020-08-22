#OOP -> object oriented programming structure. it is an approach in which entire
#		 programming is encoded by use an object with the help of which we can 
#		implement application level security, reusablity and many more implementation.

#		approach - द्रष्टिकोण 		in which - जिसमे 		entire - सम्पूर्ण	encoded - सांकेतिक भाषा

#		features of OOP's ->
#							1.class		2.object	3.encapsulation		4.polymorphism
#							5.abstraction		6.inheritance.


#difference between POP & OOP:-
#POP -> 1. it follow top to bottom approach(only problem solving approach).
#		2. modification complex.
#		3. problem solving from biggest entity.


#OOP -> 1. it follow bottom to up approach(only problem solving approach).
#		2. modification simply.
#		3. problem solving from smallest entity(objects).


#1.object -> 1. Object is real time entity because it have state(data member) and
#				functionality.
#			 2. object is runtime entity because it's carry his state& 
#				functionality one to another place.
#			3.  Object is instance(result) of class because when create object of
#				class than class is in existence.



#object --> (has) state & functionality


#		fp= open('fnm','mode')
#		fp.name()
#		fp.read()			so fp is an object.


#Class :- 1. class is a collection of similar type of object.
#    	  2. class is a collection of data member and member function.


#	syntax for class =>	
#						class class_name:
#								'class doc string'
#								class suite(data member & member function)
								
#	syntax for object =>
#						Object_name=Class_name()

#	EXA:-

class Demo:
	'this is my demo class'
	def demoData(self):
		print('This is my oop program')
obj=Demo()
obj.demoData()

# print('print object : ',obj) #memory location of obj object.

# print('type : ',type(obj))	# __main__ is module of Demo class and
# 							#	Demo is class of obj.

# print('docstring : ',Demo.__doc__)	#doc. string.

# print('class name : ',Demo.__name__) #class name

# print('module : ',Demo.__module__)	#__main__ module

# print('base : ',Demo.__base__)	# "object" is parent class of class Demo. 

# print('module : ',float.__module__)

# print('module : ',int.__module__)

# print('module : ',str.__module__)

# print('module : ',complex.__module__)

# print('base : ',float.__base__)

# print('base : ',int.__base__)

# print('base : ',str.__base__)

# print('base : ',complex.__base__) 

# print('docstring : ',float.__doc__)

# print('docstring : ',str.__doc__)

# print('docstring : ',int.__doc__)

# print('docstring : ',complex.__doc__)


# NOTE:- all predefine class's module is "builtins" and it's parent class is "object"
#	and all user define class's module is "__main__" and it's parent class is "object". 