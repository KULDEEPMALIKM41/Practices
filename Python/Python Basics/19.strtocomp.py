#This conversion is not possiable but complex string is possiable to convert str type to complex type.


a='10+5j'									#complex string
print('a= ',a) 
print('class typpe of a = ',type(a))
b=complex(a)								#this possiable
print('b= ',b)
print('class typpe of a = ',type(b))


a="10"
print("a=",a)
print("class type of a is : ",type(a))
b=complex(a)
print("b=",b)
print("class type of b is : ",type(b))





a='abc'								# string
print('a= ',a) 
print('class typpe of a = ',type(a))
b=complex(a)								#this not possiable
print('b= ',b)
print('class typpe of a = ',type(b))