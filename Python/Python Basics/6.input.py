#to take user input
a=input("enter a \n")#by default input will return string type of data in py3 
					 #but input will return similer type of data in py2. 
b=input("enter b\n")#we know that py2 support concept of py3.
print('a=  ',a)
print('b=',b)
print('add=', int(a)+int(b))#by int()function we convert str into int.


#Note:- raw_input() function is actual function of py2 for input but this 
		#function is not support in py3.
		#we know that py3 not support concept of py2. 
		#this function (raw_input()) will also return string type of data.
		
		
# for py2 program
#a=raw_input("enter a \n")   #by default input will return string his function
#b=raw_input("enter b \n")   #type of data in py2 but py3 is not support.
							 #we know that py3 not support concept of py2.
#c=int(a)+int(b)             #by int()function we convert str into int.
#print'a=',a				 #statement
#print'b=',b			     #statement
#print'Add = ',c			 #statement
