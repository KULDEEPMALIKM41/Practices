# 5.Identity Operator => This operator is use to work on referance (referance identity).
#						  id spacifie to the unic number given to each data referance.
# is and is not is identity operator.
# a=10  b=20 c=10    so ref. id of 'a' is 123456, 'b' is 123458 anc c is 123456. it mean same data
# is keep same referance but referance variable is different.

a,b,c,d,e,f,g=10,20,10,10.00,'ab','cd','ab'
print('a=%d\nb=%d\nc=%d\nd=%f\ne=%s\nf=%s\ng=%s'%(a,b,c,d,e,f,g))
print('id of a',id(a))
print('id of b',id(b))
print('id of c',id(c))
print('id of d',id(d))
print('id of e',id(e))
print('id of f',id(f))
print('id of g',id(g))
aa=a is b
bb=a is c
cc=a is d
dd=a is e
ee=a is f
ff=e is f
gg=e is g
print('a is b',aa)
print('a is c',bb)
print('a is d',cc)
print('a is e',dd)
print('a is f',ee)
print('e is f',ff)
print('e is g',gg)
aa=a is not b
bb=a is not c
cc=a is not d
dd=a is not e
ee=a is not f
ff=e is not f
gg=e is not g
print('a is not b',aa)
print('a is not c',bb)
print('a is not d',cc)
print('a is not e',dd)
print('a is not f',ee)
print('e is not f',ff)
print('e is not g',gg)