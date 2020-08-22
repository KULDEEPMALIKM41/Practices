#Range( ) -> This function is being used in python to create a coustom(user define) range.

#1.range(initialization,condition+1)

for i in range(1,11):
	print(i,end=" ")
print()



#2.range(initialization,condition+1,iteration)

for i in range(1,11,2):
	print(i,end=' ')
print()


#3.range(condition+1)

for i in range(11):
	print(i,end=' ')
print()


for i in range(-5):		#not work
	print(i,end=' ')
print()



for i in range(0):		#not work
	print(i,end=' ')	
print()




for i in range(5):
	print(i,end=' ')
print()