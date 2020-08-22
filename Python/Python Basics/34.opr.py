#6.Membership Operator => if we are to cheak the membership of one type of reference in other 
#	collection.we use menbership operator.

a='123456'
b='123'
c='456'
d='234'
e='16'
res=b in a
print('b in a',res)
res=c in a
print('c in a',res)
res=d in a
print('d in a',res)
res=e in a
print('e in a',res)
res=b not in a
print('b not in a',res)
res=c not in a
print('c not in a',res)
res=d not in a
print('d not in a',res)
res=e not in a
print('e not in a',res)