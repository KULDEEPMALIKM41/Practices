#technique of round answer in float type.
a,b=10,3
print('a=%d,\nb=%d'%(a,b))
print('Div : ',a/b)
print('floor Div : ',a//b)
print('Div : %0.3f'%(a/b))
res=a/b
new_res=round(res,5)
print('round res : ',new_res)