# 4.Logical Operator => and , or, not

#	and									 or								 	not

# A			B 		A and B	  |		A			B			A or B	  |		A		not(A)
							  
# F			F			F			F			F				F			T 			F
# F			T			F			F			T				T
# T			F			F			T			F				T			F			T
# T			T			T			T			T				T

a,b,c=10,20,5
res= b>a and b>c
print('result : ',res)

a,b,c=10,5,15
res=a>b and a>c
print('Result and = ',res)
res=a>b or a>c
print('Result or = ',res)
res=not(a>b) and not(a>c)
print('Result not = ',res)
res=not(a>b and a>c)
print('Result and,not = ',res)