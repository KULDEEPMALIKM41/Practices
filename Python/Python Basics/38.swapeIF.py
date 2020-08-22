#swapping

a=int(input('enter any number a \t'))
b=int(input('enter any number b \t'))
a,b=b,a						#change internal refernce
print('value of a is',a)
print('value of b is',b)

a=int(input('enter any number a \t'))
b=int(input('enter any number b \t'))
c=a
a=b
b=c
print('value of a is',a)
print('value of b is',b)

a=int(input('enter any number a \t'))
b=int(input('enter any number b \t'))
a=a+b
b=a-b
a=a-b
print('value of a is',a)
print('value of b is',b)