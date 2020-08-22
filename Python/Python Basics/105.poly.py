#polymorphism concept in function=>
#			polymorphism --> one name different forms.

#polymorphism --> it is an object oriented feature with signify one thing having
#					different different implementation use to achieve code reusability. 

#overloading --> it is a king of polymorphism with signify one entity different 
#			  	different implementation use to achieve code reusability.it can 
#				be implemented in two ways.
#				1. function overloading		2. operator overloading

# 1.function overloading --> in python there is a possibility to overloaded a function
#							not following traditional c++ approach but using python 
#							argument type.


#classification of overloaded function on based of argument -->

#1. default argument -->

def add(a=0,b=0,c=0,d=0,e=0):
	print('addition of = ',a+b+c+d+e)
add()
add(10)
add(10,20,30)
add(1,2,3,4,5)
#add(1,2,3,4,5,6)	#error


#2. keyword argument -->

def employee(eno,enm):
	print('employee details  : ')
	print('enm : ',enm)
	print('eno : ',eno)
employee(enm='kuldeep',eno=101)


#3. variable length argument -->

def add(*tup):
	s=0
	for element in tup:
		s=s+element
	print('add=',s)
	#print(tup)
add()
add(10)
add(10,20,30)
add(1,2,3,4,5)
add(1,2,3,4,5,6)
add(1,2,3,4,5,6,1,2,3,4,5,10,20,30)



#4. required argument -->

def add(a,b,c):
	print('addition is = ',a+b+c)
add(10,20,30)
#add(10,20)			#error
#add(10,20,30,40)	#error