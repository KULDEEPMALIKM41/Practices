#jumping Keywords
# 1. Break -> this key word is use to terminet the loop when ever executed.

#example:-
print('Before execution')
n=20
for i in range(1,101):
	if i>n:
		break  #if this keyword is execute loop's is stoped.
	print(i)
print(i)
print('Before execution \n')


# 2.continue ->This key word is use to bypass the loop execution when ever executed in loop.


#example:-
print('Before execution')
for i in range(1,101):
	if i%10!=0:
		continue	#if this keyword is execute loop's bottom part is not execute.
	print(i,end='')
	print('Hello')
print(i)

print('Before execution \n')


# 3.pass -> it is used to define empty body in a control structure .


#example:-
print('Before execution')
if 0==0:
	pass		#empty body.
print('Before execution')