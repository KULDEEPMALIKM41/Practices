#data type => it specify the type of data which is referred  by an reference variable.
#										or
#data type => in python each element is referred as an object & each object is of predefine class. 
#										or
#data type => data type specify type of data to be stored in a variable. in python each entity as a reference and data type 
# signify the type of reference which is manage internally.
# python based on smalltalk language.
#type of data types => 1.Number				 2.String 				3.sequences 				4.Boolean
#					   >integer(int)		       >string(str)			  >list(list)				  >boolean
#					   >float(float)		   						  >tuple(tuple)
#					   >complex(complex)							  >dictionary(dict)

# 1.Number =>
#				NOte:- number data type id immutable.
#
#      a) operator operation on number data type.

a=50
b=10
print('a=',a)
print('b=',b)
c=a+b
d=a-b
e=a*b
f=a/b
print('add=',c)
print('sub=',d)
print('mul=',e)
print('div=',f,'\n')

#		b)methods of number data type.

#			* modules  -> modules are collection of reference , functionality and classes.
#					
#				sys module -> if we are to get the system related specification in python there
#								is an possible to access sys module.
#								Syntax to link module:- 
#												import <module_name>
#									e.g:-
#											import sys
#								
#									Syntax to access module:-
#															module_name.property


import sys
a=0					#null integer value
print('a=',a)
print('size of a= ',sys.getsizeof(a),'\n')  #only integer class size.



import sys
a=10000					#integer value
print('a=',a)
print('size of a= ',sys.getsizeof(a),'\n')  # integer class+value size.


import sys
a=10000.00					#float value
print('a=',a)
print('size of a= ',sys.getsizeof(a),'\n')  #float class+value size.


import sys
a=10220000000+500000j					#complex value
print('a=',a)
print('size of a= ',sys.getsizeof(a),'\n')  #complex class+value size.


#								> memory view ->  1byte=8bit=256 number hold
#												1byte signed range is -128 to +127. 
#												1byte unsigned range is 0 to 255.
#
#								 		how this?
#										for signed ->	we know that 1byte = 8bit
#														
#						   so this 8 bit is ->      2@7  2@6  2@5  2@4  2@3  2@2  2@1  2@0
#										      signed bit  64 + 32 + 16 + 8 +  4  + 2  + 1 = 127
#												- or +
#    													so -128 to +127	(256 numbers)
#															-2@7 to 2@7-1
#												
#										for unsigned ->	we know that 1byte = 8bit
#														
#						   so this 8 bit is ->      2@7  2@6  2@5  2@4  2@3  2@2  2@1  2@0
#										            128 + 64 + 32 + 16 + 8 +  4  + 2  + 1 =255 
#												
#    													so  0 to  255	(256 numbers)
#															2@0 to 2@8-1


#						so on 2byte= -32768 to +32767 or -2@15 to 2@15-1
#									if unsigned => 0 to 65536  or 2@0 to 2@16-1
#										
#						  4byte= -2147483648 to +2147483647 or -2@31 to 2@31-1
#                                   if unsigned => 0 to 4294967295 or 2@0 to 2@32-1


#							> data type size in Windows:-
#
#							reference size		total size		class size 		data size
# 								int					14byte			12byte			2byte/5digit
#								float				16byte				_			   _/n digit
#								complex				24byte				_			   _/n digit
#								string				26byte			25byte			1byte/character

#							> data type size in Linex:-
#
#							reference size		total size		class size 		data size
# 								int					28byte			24byte			4byte/10digit
#								float				24byte			20byte			 4byte/n digit
#								complex				32byte				_			   _/n digit
#								string				50byte			49byte			1byte/character
#
#
#
#						Math module -> it containing multiple functionality to be implemented on
#									number data along with trigonometric operation and many more.

#type 1 for import modules
import math
a=10.99
b=-10.99
print('fabs:')				#convert into positive value.
print('a= ',math.fabs(a))
print('b= ',math.fabs(b),'\n')



#type 2 for import modules
from math import fabs		#now we are only fabs method of math module is call in this code.
a=10.99
b=-10.99
print('fabs:')				#convert into positive value.
print('a= ',fabs(a))
print('b= ',fabs(b),'\n')



#type 3 for import modules
from math import *		#now we are all methods of math module is call in this code.
a=10.11
b=-10.11
print('fabs:')				#convert into positive value.
print('a= ',fabs(a))
print('b= ',fabs(b),'\n')
print('a= ',floor(a))		#nearest small value return.
print('b= ',floor(b),'\n')
print('a= ',ceil(a))		#nearest big value return.
print('b= ',ceil(b),'\n')


#rename inbuilt module
import math as mymodule
a=10.11
b=-10.11
print('a= ',mymodule.ceil(a))
print('b= ',mymodule.ceil(b),'\n')


from math import *
a=10
b=3
print('pow :',pow(a,b),'\n')  #power


from math import *
a=100
print('sqrt :',sqrt(a),'\n') #squire root


import math
print('math :')
a=math.asin(1)				#value return in radian
b=math.acos(1)
c=math.atan(1)
print('asin :',a) 
print('acos :',b)
print('atan :',c)
print('degree of a= ',math.degrees(a))		# convert radian to degrees
print('degree of b= ',math.degrees(b))		
print('degree of c= ',math.degrees(c),'\n')


import math
a=4
b=3
h=math.hypot(a,b)	#calculate hypotenuse.
print('hypo :',h)

		
#							c) function of numbers ->

a,b,c,d,e=10,60,35,6,-25
print('max reference :',max(a,b,c,d,e))   #return maximum value
print('min reference :',min(a,b,c,d,e))	  #return minimum value
print('abs e :',abs(e))					  # convert any reference into positive


a=10.99
b=-10.99
print('round :')
print('a= ',round(a)) #nearest value of given number.
print('b= ',round(b))


#cmp function
a=10
b=20
#res=cmp(a,b)   #if b is big then function return -1,if a is big then function return 1 
#					and	if a&b is equal function is return 0. but this function is work
#						in only py2.
                  