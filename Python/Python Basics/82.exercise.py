o='y'
d=0
l=[]
while o=='y':
	print('for create list press : 1')
	print('show all list name press : 2')
	print('show all list values press : 3')
	print('for insert values press : 4')
	print('for remove values press : 5')
	print('for insert values with index no. press : 6')
	print('for remove last values press : 7')
	print('for delete list  press : 8','\n')
	c=int(input())
	if c==1:
		d=int(input('enter number of list'))
		for e in range(d):
			l.append([])
		print(e+1,'list is created')
	if c==2:
		if d==0:
			print('please create list firstly')
		else:	
			for e in range(d):
				print('list no.',e+1,'is l','[',e,']')
	if c==3:
		if d==0:
			print('please create list firstly')
		else:	
			for e in range(d):
				print('list no.',e+1,'value is',l[e])
	if c==4:
		if d==0:
			print('please create list firstly')
		else:
			e=int(input('please inseart list number : '))-1
			n=int(input('entered number of element'))
			for i in range(n):
				a=int(input('enter elements'))
				l[e].append(a)
			print('updated list l[',e,']is',l[e])
	if c==5:
		if d==0:
			print('please create list firstly')
		else:
			e=int(input('please inseart list number : '))-1
			a=int(input('element value which you are remove'))
			l[e].remove(a)
			print('updated list l[',e,']is',l[e])
	if c==6:
		if d==0:
			print('please create list firstly')
		else:
			e=int(input('please inseart list number : '))-1
			a=int(input('element value which you are insert'))
			id=int(input('enter index no'))
			l[e].insert(id,a)
			print('updated list l[',e,']is',l[e])
	if c==7:
		if d==0:
			print('please create list firstly')
		else:
			e=int(input('please inseart list number : '))-1
			l[e].pop()
			print('updated list l[',e,']is',l[e])
	if c==8:
		if d==0:
			print('please create list firstly')
		else:
			e=int(input('please inseart list number : '))-1
			del l[e]
			print('list l[',e,'] is','deleted')
			d=d-1
	o=input('do you want to take any operation press y/n   ')