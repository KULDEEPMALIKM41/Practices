# #exe7
# for i in range(1,6):
# 	for j in range(i,5):
# 		print(' ',end=' ')
# 	for k in range(1,i+1):
# 		print('*',end=' ')
# 	print()
# print()


for i in range(1,10):
	if i <= 5:
		for j in range(1,6-i):
			print('',end=' ')
		for k in range(1,i+1):
			print('*',end=' ')	
	else:
		for j in range(6,i+1):
			print('',end=' ')
		for k in range(i,10):
			print('*',end=' ')
	print()
	
#exe8
for i in range(1,6):
	for j in range(i,5):
		print(' ',end=' ')
	for k in range(1,i+1):
		print('* ',end=' ')
	print()
print()
	
	
exe9
for i in range(1,10):
	if i<6:
		for j in range(i,5):
			print(' ',end=' ')
		for k in range(1,i+1):
			print('* ',end=' ')
		print()
	else:
		for j in range(5,i):
			print(' ',end=' ')
		for k in range(i,10):
			print('* ',end=' ')
		print()
print()