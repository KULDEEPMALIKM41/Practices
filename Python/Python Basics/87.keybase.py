#key base -->

#				{[],[]}  , [{},{}] --> JSON sequence

d={'kuldeep':[78,65,82],'bharat':[60,63,74],'sanjay':[60,55,70]}
print('d is: ',d)
for key in d:
	print('details of : ',key)
	print('3 year persentage is:')
	for element in d[key]:
		print(element,end='    ')
	print('\n\n\n\n\n')
	
	
	
	
	
d=[{'name':'kuldeep','phone':8890834462,'add':'pratapgath'},
{'name':'bharat','phone':9865776354,'add':'sidhpura'},
{'name':'sanjay','phone':7023966997,'add':'dabra'}]
print('dictionary is : ',d)
for data in d:
	for key in data:
		print(key,' : ',data[key])
	print()	