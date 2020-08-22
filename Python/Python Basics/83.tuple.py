1# Tuple:- tuple is an sequence similar to that of list but there is an different in both of
#			them tuple is immutable instance but list is mutable instance.
#
#			syntax:- tup_name=(ele1,ele2,ele3....)
#
#			exam:- tuple=(10,20,30,40,50)
#					
#			tuple size:- 48byte(class) + 8byte/element
#
#			single element tuple syntax:- tup_name=(element1,)
#
#							exam:- tuple=(10,)


t=(10,20,30,40,50)
print('tuple : ',t)
print('tuple type : ',type(t),'\n')


t=(10010001,'amit',3000.11,True)
print('tuple : ',t)
print('tuple type : ',type(t),'\n')


t=(10,20,30,40,50)
print('tuple : ',t)
print('tuple menual access')
print('t[1] : ',t[1],'\n')



t=(10,20,30,40,50)
print('tuple : ',t)
print('tuple loop access by index')
for i in range(0,len(t)):      
	print(t[i],end=' ')
print('\n')


t=(10,20,30,40,50)
print('tuple : ',t)
print('tuple loop access by element')
for element in t:
	print(element,end=' ')
print('\n')
1

#						a) operator of tuple ->

#concatenation operator
t1=(10,20,30)
t2=(40,50,60)
t1=t1+t2
print('new tuple is',t1,'\n')


#multiplier operator
t1=(10,20,30)
t2=3
t=t1*t2
print('new tuple is',t,'\n')


#membership operator
t1=(10,20,30)
t2=20
t=t2 in t1
print('found',t,'\n')


t1=(10,20,30,(50,60))
t2=(50,60)
t=t2 in t1
print('found',t,'\n')


t1=(10,20,30,(50))  #(50) is an element of t1 tuple it not a single element tuple.
t2=(50)				#this fifty is int value of t2 variable.
t=t2 in t1
print('found',t,'\n')


t1=(10,20,30,(50))	#(50) is an element of t1 tuple it not a single element tuple.
t2=50				#this fifty is int value of t2 variable.
t=t2 in t1
print('found',t,'\n')



t1=(10,20,30,(50,)) #(50,)actual single element list in t1 tuple..
t2=50				#this fifty is int value of t2 variable.
t=t2 in t1
print('found',t,'\n')


t1=(10,20,30,(50,)) #(50,)actual single element tuple in t1 tuple..
t2=(50,)				#this is a single element tuple.
t=t2 in t1
print('found',t,'\n')



#range &slice operator
t=(10,20,30,40,50,60,70,80,90)
print('tuple: ',t)
print('t[2]=',t[2])
print('t[-2]=',t[-2])
print('t[1:9]=',t[1:9])
print('t[:7]=',t[:7])
print('t[3:]=',t[3:])
print('t[:]=',t[:])
print('t[-1:-10:-1]=',t[-1:-10:-1])
print('t[::-1]=',t[::-1])
print('t[::1]=',t[::1])
print('t[::]=',t[::])
print('t[-1:4:-1]=',t[-1:4:-1])
print('t[7:0:-2]=',t[7:0:-2])
print('t[1:7:2]=',t[1:7:2],'\n')

#				b)mutable and immutable -> 
#												tuple is immutable.
#
t=(10,20,30,40,50)
print(' before list: ',t)
#t[1]=100	#this operation is not perform on tuple
#del t[4]	#this operation is not perform on tuple
print(' after list: ',t,'\n')


#				c)function in tuple ->

#max and min function
t=(10,20,30,40,50)
print('tuple is : ',t)
print('maximum element is: ',max(t))
print('manimum element is: ',min(t),'\n')


t=(10010001,'amit',3000.11,True)	#string,int or float and boolean type data is not compare.
print('tuple is : ',t,'\n')
#print('maximum element is: ',max(t))
#print('minimum element is: ',min(t),'\n')



t=(10,20,30,(40,))					#error - tuple and integer not compare in tuple.
print('tuple is : ',t,'\n')
#print('maximum element is: ',max(t))
#print('minimum element is: ',min(t),'\n')


t=(10,20,30,[40])					#error - list and integer not compare in tuple.
print('tuple is : ',t,'\n')
#print('maximum element is: ',max(t))
#print('minimum element is: ',min(t),'\n')


t=(10,20,33.12,20.01,33.13)
print('tuple is : ',t)
print('maximum element is: ',max(t))
print('manimum element is: ',min(t),'\n')


#len function
t=(10010001,'amit',3000.11,True)
print('length of t = ',len(t),'\n')


#tuple and type function
s='universal'
print('s= ',s)
print('type of s: ',type(s))
l=[10,20,30,40,50]
print('l= ',l)
print('type of l: ',type(l))
t=tuple(s)
print('t= ',t)
print('type of t: ',type(t),'\n')
t=tuple(l)
print('t= ',t)
print('type of t: ',type(t),'\n')

#id function
t1=(10010001,'amit',3000.11,True)
t2=(10,20,33.12,20.01,33.13)	
t3=(10,20,30,[40])
t4=(10010001,'amit',3000.11,True)
t5=(10,20,33.12,20.01,33.13)	
t6=(10,20,30,[40])
print('id of t1',id(t1))
print('id of t2',id(t2))	#Note:- same sequence data different different reference.
print('id of t3',id(t3))
print('id of t4',id(t4))
print('id of t5',id(t5))
print('id of t6',id(t6),'\n')


#							d)method in tuple ->

import sys
t1=(10010001,'amit',3000.11,True)
t2=(10,20,33.12,20.01,33.13)	
t3=(10,20,30,[40])
t4=()
print('size of t1 : ',sys.getsizeof(t1))		#tuple class+value size
print('size of t2 : ',sys.getsizeof(t2))		#tuple class+value size
print('size of t3 : ',sys.getsizeof(t3))		#tuple class+value size
print('size of t4 : ',sys.getsizeof(t4),'\n')	#tuple class size

#Note:- 1) ubuntu
#					type		total size		class size		data size	
#
#					tuple		 56 byte		  48 byte		 8 byte/element
#
#		2) windows
#					tuple		 32 byte		   28 byte		 4 byte/element



#index method
t=(20,10,30,50,40,10,20,50)
print('tuple is : ',t)
n=t.index(10)
print('found index: ',n)
n=t.index(40)			#return first element index number.
print('found index: ',n)
#n=t.index(70)				#if element is not found it will give error.
#print('found index: ',n)
n=t.index(30,2)				#search after index number 1.
print('found index: ',n,'\n')
n=t.index(50,1,4)			#search between 1to 4index number.
print('found index: ',n)


#count method
t=(20,10,30,50,40,10,20,50)
print('tuple is : ',t)
n=t.count(50)				#total number of 50 in tuple.
print('total number: ',n)

#copy method --> this method is not work on tuple
''''t1=(10010001,'amit',3000.11,True)
print(t1)
print('id of t1',id(t1))
t2=t1						#in this type copy data store in same reference id.
print(t2)
print('id of t2',id(t2))
t2=t1.copy()					#in this type copy data store in deferent reference id.
print(t2)
print('id of t2',id(t2),'\n')
'''


#reverse method  --> this method is not work on tuple
'''t=(10,20,30,40,50)
print('before revers : ',t)
t.reverse()
print('after revers : ',t,'\n')
'''

#sort method -->  this method is not work on tuple
'''t=(20,10,30,50,40)
print('before sort(ascending) : ',t)
t.sort()					            #ascending order(by default).
print('after sort(ascending) : ',t,'\n')
'''


#insert method --> this method is not work on tuple
'''t=(20,10,30,50,40)
print('tuple is : ',t)
t.insert(2,100)						#write index no. then write value.
print('after insertion : ',t,'\n')
'''


#remove method --> this method is not work on tuple
'''t=(20,10,30,50,40)
print('tuple is : ',t)
t.remove(50)						#remove number bye his value.
print('after remove : ',t,'\n')
'''


#POP method --> this method is not work on tuple
'''t=(20,10,30,50,40)
print('tuple is : ',t)
t.pop()						#in tuple last value is deleted.
print('after pop : ',t,'\n')
'''



#del keyword not a method
'''t=(20,10,30,50,40)
print('list is : ',t)
del t[3]							#delete any index value.
print('after delete : ',t,'\n')
'''

#del keyword not a method
t=(20,10,30,50,40)
print('tuple is : ',t)
del t								#list l is deleted and not existence in code.
#print('after delete : ',t,'\n')


#append method --> this method is not work on tuple.
'''t=(20,10,30,50,40)
print('tuple is : ',t)
t.append(60)
t.append(70)
t.append(80)					     	#add value in last of tuple.
print('after 3 time append : ',t,'\n')
'''


#encoding and decoding not support for list.
'''t=(20,10,30,50,40,10,20,50)
print('actual list: ',t)
t=t.encode('utf-8')				#encoding
print('encoded list: ',t)
t=t.decode('utf-8')				#decoding
print('decoded list: ',t)'''


#rindex method --> this method is not support in tuple.
'''t=(20,10,30,50,40,10,20,50)
print('tuple is : ',t)
n=t.rindex(10)
print('found index: ',n)
n=t.index(40)			#return first element index number.
print('found index: ',n)
#n=t.index(70)				#if element is not found it will give error.
#print('found index: ',n)
n=t.index(30,2)				#search after index number 1.
print('found index: ',n,'\n')
n=t.index(50,1,4)			#search between 1to 4index number.
print('found index: ',n)'''


#find method --> this is not support in tuple.
'''t=(20,10,30,50,40,10,20,50)
n=t.find('50')
print('found index: ',n)'''


#rfind method --> this is not support in tuple.