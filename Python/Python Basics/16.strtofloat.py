#This conversion is not possiable but numerical string is possiable convert str type to float type.


a='10.5'								#float numerical string
print('a= ',a) 
print('class typpe of a = ',type(a))
b=float(a)								#this possiable
print('b= ',b)
print('class typpe of a = ',type(b))


a='10'								#intger numerical string
print('a= ',a) 
print('class typpe of a = ',type(a))
b=float(a)								#this possiable
print('b= ',b)
print('class typpe of a = ',type(b))


a='abc' 								#string
print('a= ',a)
print('class typpe of a = ',type(a))
b=float(a)								#not possiable
print('b= ',b)
print('class typpe of a = ',type(b))