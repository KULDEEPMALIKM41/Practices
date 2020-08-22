# File => file is an storage capable to store bulk amount of data  a particular
#		location. this storage can be used to manage large amount of unstructure
#		data.to manage this kind of storage file handling is use.

#open file:-
#			file reference=Open('file name','operation mode')

# file mode for plain text data =>

#	r -> read (if file is not exist this mode is generate error)

#	w -> write (if file is not exist this mode is create new file & if file
#		 already exist than file is replace.)

#	a -> append (if file is not exist this mode is create new file & if file
#		 is already exist than file is update and old data is not remove.)

# file mode for binary data =>

#							br, bw, ba (same work as r, w, a modes)

#example:-

fp= open('data.txt','w')
print('file referance : ' ,fp) # _io <-- module of TextIOWrapper class & 
						   # fp its class object.
print('type of fp : ',type(fp))

print('file name : ',fp.name)	#'name' is parameter

print('file mode : ',fp.mode)	#'mode' is parameter

print('file closed : ',fp.closed)	#'closed' is parameter

print('\n\n\n')


#example:-

fp=open('data.txt','w')
file_data="""OOP -> object oriented programming structure. it is an approach in which entire
		 programming is encoded by use an object with the help of which we can 
		implement application level security, reusablity and many more implementation.

		features of OOP's ->
							1.class		2.object	3.encapsulation		4.polymorphism
							5.abstraction		6.inheritance.


difference between POP & OOP:-
POP -> 1. it follow top to bottom approach(only problem solving approach).
		2. modification complex.
		3. problem solving from biggest entity.


OOP -> 1. it follow bottom to up approach(only problem solving approach).
		2. modification simply.
		3. problem solving from smallest entity(objects).


1.object -> 1. Object is real time entity because it have state(data member) and
				functionality.
		 2. object is runtime entity because it's carry his state& 
				functionality one to another place.
			3.  Object is instance(result) of class because when create object of
				class than class is in existence.



object --> (has) state & functionality


		fp= open('fnm','mode')
		fp.name()
		fp.read()			so fp is an object.


Class :- 1. class is a collection of similar type of object.
    	  2. class is a collection of data member and member function.


	syntax for class =>	
						class class_name:
								'class doc string'
								class suite(data member & member function)
							
	syntax for object =>
						Object_name=Class_name()"""
fp.write(file_data)
print('content insert inside file')
fp.close()
print('file closed : ',fp.closed)

print('\n\n\n')



#example:-

fp=open('data.txt','a')
file_data="""OOP -> object oriented programming structure. it is an approach in which entire
		 programming is encoded by use an object with the help of which we can 
		implement application level security, reusablity and many more implementation.

		features of OOP's ->
							1.class		2.object	3.encapsulation		4.polymorphism
							5.abstraction		6.inheritance.
"""
fp.write(file_data)
print('content insert inside file')
fp.close()
print('file closed : ',fp.closed)



#example:-

fp=open('data.txt','r')
file_data=fp.read()
print('file content: ',file_data)
fp.close()
print('file closed : ',fp.closed)

print('\n\n\n')


#example:-

fp=open('data.txt','r')
file_data=fp.read(100) #first 100 character read
print('file content: ',file_data)
fp.close()
print('file closed : ',fp.closed)

print('\n\n\n')



#example:-
try:
	fp=open('data1.txt','r')
	file_data=fp.read()
	print('file content: ',file_data)
	fp.close()
except FileNotFoundError:
	print('file is not in existance')
print('\n\n\n')


#example:-

fp=open('data.txt','r')
print('file ptr position: ',fp.tell())
file_data=fp.read(20) #first 20 character read
print('file content: ',file_data)
print('file ptr position: ',fp.tell())
fp.seek(0)
file_data=fp.read(20)
print('file content: ',file_data)
print('file ptr position: ',fp.tell())
fp.close()
print('\n\n\n')