
# 7.Bitwise Operator => & (Bitwise and) , | (Bitwise or), ^ (Bitwise XOR), 
# ~ ( Bitwise once complement), << (Bitwise left shift) , >> (Bitwise right shift)
# Bit's Repersentation 2 POWER
#  <-.......... 128		64		32		16		8		4		2		1......->
#<-......MSB														LSB......->
#a=21 -> 0	0	0	1	0	1	0	1
#b=13 -> 0	0	0	0	1	1	0	1
#a&b  -> 0	0	0	0	0	1	0	1 ->05
#a|b  -> 0	0	0	1	1	1	0	1 ->29
#a^b  ->0	0	0	1	1	0	0	0 ->24
# ~a  -> -(a+1)						  ->-22
#a<<3 -> a= 			0	0	0	1	0	1	0	1
#			0	0	0	1	0	1	0	1	0	0	0	<-   SHIFT 3 BIT
#						128		32		8			  = 168

#Bit's Operational Table
#a		b		a&b		a|b		a^b
#0		0		0		0		0
#0		1		0		1		1
#1		0		0		1		1
#1		1		1		1		0

a=int(input('enter any number a \t'))
b=int(input('enter any number b \t'))
print('a&b',a&b)
print('a|b',a|b)
print('a^b',a^b)
print('~a',~a)
print('a<<3',a<<3)
print('a>>3',a>>3)
