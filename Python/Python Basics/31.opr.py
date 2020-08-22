# 3.Comparision Operator => ( ==,	>,	<,	>=,	<=,	!= ) this operator is compair two referance value and
#							( === ) operator is compair two referance value with data type.

a,b=10,20
print('a=%d\nb=%d'%(a,b))
res=a>b
print('result a>b : ',res)
print('Type of result : ',type(res))
print('result a<b :',a<b)
print('result a>=b :',a>=b)
print('result a<=b :',a<=b)
print('result a!=b :',a!=b)

a,b=10,10.00
print('a=%d\nb=%f'%(a,b))
print('result a==b :',a==b)

#true & false is boolean type data type.