#nested sequence =>

#          [],()  --> index base		{} --> key base

#			Index base -->
#							[[],[]] , [(),()] , ((),()) , ([],[])

d=[[10,20,30],[40,50,60],[70,80,90]]
print('menual access')
print(d[2])
print(d[1][2],'\n')


d=[[10,20,30],[40,50,60],[70,80,90]]
print('loop access')
for i in d:
	for element in i:
		print('element : ',element,end='      ')
	print()
	
d=[(10,20,30),(40,50,60),[70,80,90]]
print('loop access')
for i in d:
	for element in i:
		print('element : ',element,end='      ')
	print()
	
	
d=((10,20,30),(40,50,60),[70,80,90])
print('loop access')
for i in d:
	for element in i:
		print('element : ',element,end='      ')
	print()