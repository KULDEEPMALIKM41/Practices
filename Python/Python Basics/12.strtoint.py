#This conversion is not possiable but numerical string is possiable to convert str type to int type.


a='10'									#numerical string
print('a= ',a) 
print('class typpe of a = ',type(a))
b=int(a)								#this possiable
print('b= ',b)
print('class typpe of a = ',type(b))


a='abc' 								#string
print('a= ',a)
print('class typpe of a = ',type(a))
b=int(a)								#not possiable
print('b= ',b)
print('class typpe of a = ',type(b))