import random
for i in range(10):
	print(random.random())		#by default random.random() return value between 0 to 1.
print()

for i in range(10):
	print(random.random()*1000000)
print()	

for i in range(10):
	print(int(random.random()*1000000))
print()	

for i in range(10):
	print(4*random.random()+3) #3 is starting number & 4 is limit.
print()	
	
for i in range(10):
	print(random.uniform(3,7)) #same as 4*random.random()+3
print()

for i in range(10):
	print(random.randint(0,9)) #return 0 to 9 integer no.
print()

list1=['kuldeep','sanjay','rahul','bharat']
for i in range(10):
	print(random.choice(list1)) #choice any index no.
print()

print(random.sample(list1,2))

















