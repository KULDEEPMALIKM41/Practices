# python sequence ->
#					sequence are collection capable to store bulk amount of data
#						simultaneously.in python collection have capability to store 
#						heterogeneous reference simultaneously.
#
#				NOTE:- as per storage type the collection may vary.

#			1.list sequence		2.tuple sequence	3.dictionary sequence
#
#
# 1. list sequence ->
#					list is an collection  capable to store multiple heterogeneous reference
#					simultaneously each reference in a list will be given by an integer number.
#
#					syntax:-
#							list_name=[ele1,ele2,ele3....]
#
#							ele1,ele2,ele3... -> these are heterogeneous elements.
#
l=[10,20,30,40,50]
print('list : ',l)
print('list type : ',type(l),'\n')


l=[10010001,'amit',3000.11,True]
print('list : ',l)
print('list type : ',type(l),'\n')


l=[10,20,30,40,50]
print('list : ',l)
print('list menual access')
print('l[1] : ',l[1],'\n')



l=[10,20,30,40,50]
print('list : ',l)
print('list loop access by index')
for i in range(0,len(l)):      
	print(l[i],end=' ')
print('\n')


l=[10,20,30,40,50]
print('list : ',l)
print('list loop access by element')
for element in l:
	print(element,end=' ')
print('\n')


#						a) operator of list ->

#concatenation operator
l1=[10,20,30]
l2=[40,50,60]
l=l1+l2
print('new list is',l,'\n')


#multiplier operator
l1=[10,20,30]
l2=3
l=l1*l2
print('new list is',l,'\n')


#membership operator
l1=[10,20,30]
l2=20
l=l2 in l1
print('found',l,'\n')


l1=[10,20,30,[40]]
l2=40
l=l2 in l1
print('found',l,'\n')


l1=[10,20,30,[40]]
l2=[40]
l=l2 in l1
print('found',l,'\n')


#range &slice operator
l1=[10,20,30,40,50,60,70,80,90]
print('list: ',l1)
print('l1[2]=',l1[2])
print('l1[-2]=',l1[-2])
print('l1[1:9]=',l1[1:9])
print('l1[:7]=',l1[:7])
print('l1[3:]=',l1[3:])
print('l1[:]=',l1[:])
print('l1[-1:-10:-1]=',l1[-1:-10:-1])
print('l1[::-1]=',l1[::-1])
print('l1[::1]=',l1[::1])
print('l1[::]=',l1[::])
print('l1[-1:4:-1]=',l1[-1:4:-1])
print('l1[7:0:-2]=',l1[7:0:-2])
print('l1[1:7:2]=',l1[1:7:2],'\n')

#				b)mutable and immutable -> 
#	 												list is mutable.
#
l=[10,20,30,40,50]
print(' before list: ',l)
l[1]=100
del l[4]
print(' after list: ',l,'\n')



#				c)function in list ->

#max and min function
l=[10,20,30,40,50]
print('list is : ',l)
print('maximum element is: ',max(l))
print('manimum element is: ',min(l),'\n')


l=[10010001,'amit',3000.11,True]	#string,int or float and boolean type data is not compare.
print('list is : ',l,'\n')
#print('maximum element is: ',max(l))
#print('manimum element is: ',min(l),'\n')



l=[10,20,30,[40]]					#error - list and integer not compare.
print('list is : ',l,'\n')
#print('maximum element is: ',max(l))
#print('manimum element is: ',min(l),'\n')



l=[10,20,33.12,20.01,33.13]	
print('list is : ',l)
print('maximum element is: ',max(l))
print('manimum element is: ',min(l),'\n')


#len function
l=[10010001,'amit',3000.11,True]
print('length of l = ',len(l),'\n')

#list and type function
s='universal'
print('s= ',s)
print('type of s: ',type(s))
l=list(s)
print('l= ',l)
print('type of l: ',type(l),'\n')

#id function
l1=[10010001,'amit',3000.11,True]
l2=[10,20,33.12,20.01,33.13]	
l3=[10,20,30,[40]]
l4=[10010001,'amit',3000.11,True]
l5=[10,20,33.12,20.01,33.13]	
l6=[10,20,30,[40]]
print('id of l1',id(l1))
print('id of l2',id(l2))	#Note:- same sequence data different different reference.
print('id of l3',id(l3))
print('id of l4',id(l4))
print('id of l5',id(l5))
print('id of l16',id(l6),'\n')


#							d)method in list ->

import sys
l1=[10010001,'amit',3000.11,True]
l2=[10,20,33.12,20.01,33.13]	
l3=[10,20,30,[40]]
l4=[]
print('size of l1 : ',sys.getsizeof(l1))		#list class+value size
print('size of l2 : ',sys.getsizeof(l2))		#list class+value size
print('size of l3 : ',sys.getsizeof(l3))		#list class+value size
print('size of l4 : ',sys.getsizeof(l4),'\n')	#list class size

#Note:- 1) ubuntu
#					type		total size		class size		data size	
#
#					list		 72 byte		  64 byte		 8 byte/element
#
#		2) windows
#					list		 40 byte		   36 byte		 4 byte/element



#copy method
l=[10010001,'amit',3000.11,True]
print(l)
print('id of t',id(l))
t=l						#in this type copy data store in same reference id.
print(t)
print('id of t',id(t))
t=l.copy()					#in this type copy data store in deferent reference id.
print(t)
print('id of t',id(t),'\n')


#reverse method
l=[10,20,30,40,50]
print('before revers : ',l)
l.reverse()
print('after revers : ',l,'\n')


#sort method
l=[20,10,30,50,40]
print('before sort(ascending) : ',l)
l.sort()					            #ascending order(by default).
print('after sort(ascending) : ',l,'\n')



#reverse&sort method
l=[20,10,30,50,40]
print('before sort(descending) : ',l)
l.sort()
l.reverse()				            	# for descending order.
print('after sort(descending) : ',l,'\n')



#insert method
l=[20,10,30,50,40]
print('list is : ',l)
l.insert(2,100)						#write index no. then write value.
print('after insertion : ',l,'\n')



#remove method
l=[20,10,30,50,40]
print('list is : ',l)
l.remove(50)						#remove number bye his value.
print('after remove : ',l,'\n')



#POP method
l=[20,10,30,50,40]
print('list is : ',l)
l.pop(1)						#removes and returns element having given index otherwise
print('after pop : ',l)			# by default last  value is remove.
r=l.pop(1)						#removes and returns element having given index otherwise
print('after pop : ',r)			# by default last  value is remove.
print('after pop : ',l,'\n')


#del keyword not a method
l=[20,10,30,50,40]
print('list is : ',l)
del l[3]							#delete any index value.
print('after delete : ',l,'\n')


#del keyword not a method
l=[20,10,30,50,40]
print('list is : ',l)
del l								#list l is deleted and not existence in code.
#print('after delete : ',l,'\n')


#append method 
l=[20,10,30,50,40]
print('list is : ',l)
l.append(60)
l.append(70)
l.append(80)					     	#add value in last of list.
print('after 3 time append : ',l,'\n')

#index method
l=[20,10,30,50,40,10,20,50]
n=l.index(10)
print('found index: ',n)
n=l.index(40)			#return first element index number.
print('found index: ',n)
#n=l.index(70)				#if element is not found it will give error.
#print('found index: ',n)
n=l.index(30,2)				#search after index number 1.
print('found index: ',n,'\n')
n=l.index(50,1,4)			#search between 1to 4index number.
print('found index: ',n)

#count method
l=[20,10,30,50,40,10,20,50]
print('list is : ',l)
n=l.count(10)				#total number of 10 in list.
print('total number: ',n,'\n')


#clear method
l=[20,10,30,50,40,10,20,50]
print('list is : ',l)
l.clear()
print('list is : ',l)

#encoding and decoding not support for list.
'''l=[20,10,30,50,40,10,20,50]
print('actual list: ',l)
l=l.encode('utf-8')				#encoding
print('encoded list: ',l)
l=l.decode('utf-8')				#decoding
print('decoded list: ',l)'''



#rindex method --> this method is not work on list.
'''l=[20,10,30,50,40,10,20,50] 
n=l.rindex(10)
print('found index: ',n)
n=l.rindex(40)			#return first element index number.
print('found index: ',n)
#n=l.rindex(70)				#if element is not found it will give error.
#print('found index: ',n)
n=l.rindex(30,2)				#search after index number 1.
print('found index: ',n,'\n')
n=l.rindex(50,1,4)			#search between 1to 4index number.
print('found index: ',n)'''

# find method --> this method is not work on list.
# rfind method --> this method is not work on list.
