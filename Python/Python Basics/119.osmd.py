# OS Module =>  This module is contain multiple functionality related
# 				to get operating system related specifications like 
#				file path, folder path  and many more.

#Example:-

import os
#os.mkdir('myimages')

path=os.getcwd()	#cwd-> current working directory
print(path)

#os.chdir('myimages')
#path=os.getcwd()
#print(path)
#os.remove('myimages')
#os.rename('data.txt','demo.txt')
#os.remove('demo.txt')