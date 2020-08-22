#Dictionary => it is an sequence capable to store multiple heterogeneous reference simultaneously
#				but apart from list and tuple dictionary storage is completely different.
#			  *apart from list and tuple dictionary manages its all internal reference by using 
#				key value pair,apart from indexing.*
#
#			syntax:- dict_name={ele1,ele2....}
#			
#					ele1= key1:value1				key ->starting indexing
#					ele2= key2:value2				value -> data to be stored
#					
#  			e.g -> d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
#
#			dictionary size => default size is 240byte.
#
#			*dictionary reference which refer all the class*


emp_details={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('dictionary is ',emp_details)
print('manual access')
print('eno:',emp_details['eno'],'\n')

	
	

emp_details={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('dictionary is ',emp_details)
print('loop access')
for key in emp_details:
	print(key,':',emp_details[key],'\n')
	
	
#bug
emp_details={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print(emp_details)
emp_details={'eno':1001001,'enm':'kuldeep','esal':10000.11,'enm':'bharat'} #same keyword
print(emp_details,'\n') #first 'enm' key word value 'kuldeep' is replace bye new value 'bharat'.


	
#							a)mutability and immutability in dictionary

#					the dictionary shows the behavior in deferent implement that is the
#					dictionary keys are immutable while dictionary value is mutable.  

	
emp_details={'eno':1001001,'enm':'kuldeep','esal':10000.11}	
print('emp_details:',emp_details)
emp_details['eno']=111111
emp_details['eadd']='pratapgarh Rajasthan'
print('emp_details:',emp_details,'\n')


#							b) operator for dictionary

#concatenation operator + --> not support this operator in dictionary.
'''emp1={'eno':1001001,'enm':'kuldeep','esal':10000.11}	
emp2={'eadd':'pratapgarh Rajasthan'}
emp=emp1+emp2
print('emp =',emp)'''



#multiplier operator --> not support this operator in dictionary.
''''emp1={'eno':1001001,'enm':'kuldeep','esal':10000.11}	
emp2=3
emp=emp1*emp2
print('emp =',emp)'''

#membership operator
emp1={'eno':1001001,'enm':'kuldeep','esal':10000.11}
emp2='eno'
emp=emp2 in emp1		#membership operator only work on keys no that on values. 
print(emp,'\n')

#range operator
emp1={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('emp1 : ',emp1)
print('eno : ',emp1['eno'],'\n') #only work range operator no that slice operator.


#						c)function in dictionary =>

#max and min function
emp1={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('dictionary is : ',emp1)
print('max: ',max(emp1)) #this function return value based on key's ASCII value in dictionary.
print('min: ',min(emp1),'\n')

#len function
emp1={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('dictionary is : ',emp1)
print('len of emp1: ',len(emp1),'\n')

#type function
emp1={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('dictionary is : ',emp1)
print('data type of dict. : ',type(emp1),'\n')

#id function
emp1={'eno':1001001,'enm':'kuldeep','esal':10000.11}
emp2={'eno':1001001,'enm':'kuldeep','esal':10000.11}
emp3={'enm':'bharat','eno':101,'esal':1000.5}
print('emp1: ',emp1,'\nemp2: ',emp2,'\nemp3: ',emp3)
print('emp1 id : ',id(emp1)) #emp1 and emp2 same data but its id is deferent.
print('emp2 id : ',id(emp2))
print('emp3 id : ',id(emp3),'\n')


#dict function --> only dictionary format element convert into dictionary.
dict=dict(name = "John", age = 36, country = "Norway")
print('dict is : ',dict)
print('data type of dict : ',type(dict),'\n')


#							d)method in dictionary ->

import sys
d1={'eno':1001001,'enm':'kuldeep','esal':10000.11}
d2={'eno':1001001}	
d3={}
print('size of d1 : ',sys.getsizeof(d1))		#dictionary class+value size
print('size of d2 : ',sys.getsizeof(d2))		#dictionary class+value size
print('size of d3 : ',sys.getsizeof(d3),'\n')	#dictionary class+value size

#Note:- 1) ubuntu
#					type		total size	
#
#				 dictionary		 240 byte
#
#		2) windows
#				 dictionary		 136 byte


#values method
d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('d is',d)
print('d of values: ',d.values(),'\n')
t=d.values()
print('type t: ',type(t),'\n')


#keys method
d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('d is',d)
print('d of values: ',d.keys(),'\n')
t=d.keys()
print('type t: ',type(t),'\n')
"""	
#get method
d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('d is',d)
print('enm:',d.get('enm'),'\n')  #get value


#item method
d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('d is',d)
print(d.items(),'\n') 
t=d.items()
print('type d: ',type(t),'\n')


#update method
d1={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('d1 is: ',d1)
d2={'eadd':'pratapgarh'}
d1.update(d2)
print(' update d1 is : ',d1,'\n\n')


#copy method 
d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print(d)
print('id of d',id(d))
d1=d						#in this type copy data store in same reference id.
print(d1)
print('id of d1',id(d1))
d1=d.copy()					#in this type copy data store in deferent reference id.
print(d1)
print('id of d1',id(d1),'\n')


#POP method
d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('dict is : ',d)
d.pop('eno')						#removes and returns element having given key 
print('after pop : ',d,'\n')
r=d.pop('enm')						#removes and returns element having given key 
print('after pop : ',r,'\n')
print('after pop : ',d,'\n')



#del keyword not a method
d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('dict is : ',d)
del d['esal']							#delete any index value.
print('after delete : ',d,'\n')


#del keyword not a method
d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('d is : ',d)
del d								#list l is deleted and not existence in code.
#print('after delete : ',d,'\n')



#index method -->this method not available in dictionary. 
'''d1={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('d1 is : ',d1)
n=d1.index(1001001)		#return first element index number.
print('found index: ',n)'''



#count method -->this method not available in dictionary.
'''d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('d is : ',d)
n=d.count(1001001)				#total number of 50 in tuple.
print('total number: ',n)'''



#reverse method  --> this method is not work on dictionary
'''d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('before revers : ',d)
d.reverse()
print('after revers : ',d,'\n')'''


#sort method -->  this method is not work on dictionary
'''d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('before sort(ascending) : ',d)
d.sort()					            #ascending order(by default).
print('after sort(ascending) : ',d,'\n')'''


#insert method --> this method is not work on dictionary
'''d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('dict is : ',d)
d.insert(eadd,prtapgarh)						#write index no. then write value.
print('after insertion : ',d,'\n')'''



#remove method --> this method is not work on dictionary
'''d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('dict is : ',d)
d.remove(1001001)						#remove number bye his value.
print('after remove : ',d,'\n')
'''





#append method --> this method is not work on dictionary.
'''d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('dict is : ',d)
d.append('eadd':pratapgarh)					     	#add value in last.
print('after  time append : ',d,'\n')'''


#encode and decode --> this method is not work on dictionary.
'''d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
print('actual list: ',d)
d=d.encode('utf-8')				#encoding
print('encoded list: ',d)
d=d.decode('utf-8')				#decoding
print('decoded list: ',d)'''



#rindex method --> this method is not support in dictionary.




#find method --> this is not support in tuple.
'''d={'eno':1001001,'enm':'kuldeep','esal':10000.11}
n=d.find('1001001')
print('found index: ',n)'''


#rfind method --> this is not support in tuple.'''


"""