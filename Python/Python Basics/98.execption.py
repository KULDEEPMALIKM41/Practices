# exception => this are an unwanted situation of programming when implemented will restrict
#				normal script execution.
#				to manage the exception so that normal flow of the script must be 
#				managed properly we use exception handling.

#	NOTE:-		in python whenever a exception will be raised.it will be the kind of 
#				reference to a predefine exception class.


#exception type  => 1. NameError	2. IndexError	3. KeyError		4. ValueError

#					5. AttributeError 		6.ImportError			7. IOError

#					8. ZeroDivisionError	9.AssertionError-user define custom error

#					10. ModuleNotFoundError	11.FileNotFoundError


#case 1

#print(a) #'print (a)' is reference or object of predefine 'NameError' class.
#print(b) #'print(b)' is reference or object of predefine 'NameError' class.



#case 2

#l=[10,20,30]
#print(l[10])	#IndexError



#case3

#emp={'eno':10101,'enm':'KULDEEP'}
#print(emp['eno1'])						#KeyError



#case4

#a=10
#b=0
#c=a/b
#print(c)



#case5

#open('demo.txt','r') 		#py3 -> FileNotFoundError ,py2 -> IOError




#case6

#def demo():
#	print('hello')
#demo(10)					#TypeError



#case7

#import math1		#ModuleNotFoundError




#case8

#import math
#math.abs(10.11)		#AttributeError

