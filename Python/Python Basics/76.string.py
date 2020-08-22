# Note:-
#	  *IDE stand for Integrated Development Environment tool.it is python coding advance tool.
#		Types of IDE->
#						1.IDLE		2.PyCharm		3.Anaconda
#
#	  *IDLE installation  command in ubuntu for py3 ->
#										"sudo apt-get install idle3"




# 2.String -> string is an reference with signify the collection of multiple string reference
#				simultaneously.
#
#				a) mutability & immutability ->
#								object is an entity which contain it's own state(data member)
#						along with behavior(functionality). if any of change made in state of
#						object and the object shows reflection than it is mutable and if not,
#						immutable. 
#
#
s='hello'
print('s=',s)
print('s[0]=',s[0])
print('s[1]=',s[1])
print('s[2]=',s[2])
print('s[3]=',s[3])
print('s[4]=',s[4],'\n')
# s[1]='p'           #error because string is immutable.


s='hello'
print('s=',s)
print('s[1]=',s[1])
print('s[2]=',s[2])
# del s[2]			#error because string is immutable.
print('s[4]=',s[4],'\n')        


# #				b)Operators for string ->
# #									
# # concatenation operator +

# s1='universal'
# s2='informetic'
# s=s1+' '+s2			
# print('s=',s,'\n')


# # multiplier operator *

# s1='universal'
# s2=3
# s=(s1+' ')*s2
# print('s=',s,'\n')



# # membership operator in,not in

# s1='universal'
# s2='niv'
# res=s2 in s1
# print('result=',res)
# res=s2 not in s1
# print('result=',res,'\n')


# # range operator  []range operator, [ : ][ : :] range slice operator.
# s='universal'
# print('s=',s)
# print('s[2]=',s[2])
# print('s[-2]=',s[-2])
# print('s[1:7]=',s[1:9])
# print('s[:7]=',s[:7])
# print('s[3:]=',s[3:])
# print('s[:]=',s[:])
# print('s[-1:-10:-1]=',s[-1:-10:-1])
# print('s[::-1]=',s[::-1])
# print('s[::1]=',s[::1])
# print('s[::]=',s[::])
# print('s[-1:4:-1]=',s[-1:4:-1])
# print('s[7:0:-2]=',s[7:0:-2])
# print('s[1:7:2]=',s[1:7:2],'\n')

# #		Note:- in python sequence do follows built in reverse indexing.



# #				c)function for string ->		
# #

# #len() function
# s='universal'
# print('s=',s)
# print('string element access loop')
# for i in range(0,len(s)):      #	by indexing
# 	print(s[i],end=' ')
# print()
# #or
# for element in s:
# 	print(element,end=' ')
# print('\n')


# #len() function
# s='universal'
# print('length of s = ',len(s),'\n')

# #max &min function( overloaded function)
# s='universal'
# print('maximam element of string: ',max(s))	#maximum ASCII number character 
# print('manimam element of string: ',min(s))	#maximum ASCII number character

# print('maximam element of string: ',max('amit','pen','x-man'),'\n')	 



# #id function
# s1='universal'
# s2='informatic'
# s3='universal'
# print('id of s1: ',id(s1))
# print('id of s2: ',id(s2))
# print('id of s3: ',id(s3),'\n')


# #str() function
# s1='universal'
# a=10
# b=10+5j
# print('convert into string s1: ',str(s1))
# print('convert into string a: ',str(a))
# print('convert into string: b',str(b),'\n')

# #type function
# s1='universal'
# a=10
# b=10+5j
# s1='universal'
# a=10
# b=10+5j
# print('s1=',s1)
# print('a=',a)
# print('b=',b)
# print('type s1=',type(s1))
# print('type a=',type(a))
# print('type b=',type(b))
# s1=str(s1)
# a=str(a)
# b=str(b)
# print('convert into string s1: ',s)
# print('convert into string a: ',a)
# print('convert into string: b',b)
# print('type s1=',type(s1))
# print('type a=',
# type(a))
# print('type b=',type(b),'\n')


# #cmp function
# s1='kuldeep'
# s2='bharat'
# #res=cmp(s1,s2) #if s2 is big then function return -1,if s1 is big then function return 1 
# #					and	if s1 s2 is equal function is return 0. but this function is work
# #						in only py2.



# #						d)method of string ->


# import sys
# a='universal'					#string value
# print('a=',a)
# print('size of a= ',sys.getsizeof(a),'\n')  # string class+value size.



# import sys
# a=''					# null string value
# print('a=',a)
# print('size of a= ',sys.getsizeof(a),'\n')  #only string class size.


# s='universal'
# print('upper case :',s.upper())
# s='HELLO'
# print('lower case :',s.lower())
# s='universal informatic'
# print('title case :',s.title())
# print('capitalize case :',s.capitalize())
# print('center case :',s.center(30,'*'),'\n')


# s1='HELLO'
# print('is upper case :',s1.isupper())
# s1='universal'
# print('is lower case :',s1.islower())
# s1='Universal Informatic'
# print('is title case :',s1.istitle())
# s1='Universal informatic'
# #print('is capitalize case :',s1.iscapitalize()) #not available
# s1='*****HELLO*****'
# #print('is center case :',s1.iscenter())			#not available
# s1=' '
# print('is space case :',s1.isspace())
# s1='12345'
# print('is numeric case :',s1.isnumeric())
# s1='123kul'
# print('is alphanumeric :',s1.isalnum(),'\n')



# s='universal informatic'
# n=s.find('l')
# print('found index: ',n)
# n=s.find('infor')			#return first character index number.
# print('found index: ',n)
# n=s.find('p')				#if substring is not found it will give return -1.
# print('found index: ',n)
# n=s.find('r',7)				#search after index number 7.
# print('found index: ',n)
# n=s.find('i',3,10)			#search between 3to 10index number.
# print('found index: ',n,'\n')


# s='universal informatic'
# n=s.index('l')
# print('found index: ',n)
# n=s.index('infor')			#return first character index number.
# print('found index: ',n)
# #n=s.index('p')				#if substring is not found it will give error.
# #print('found index: ',n)
# n=s.index('r',7)				#search after index number 7.
# print('found index: ',n,'\n')
# #n=s.index('i',3,10)			#search between 3to 10index number. this is give error because substring
# #print('found index: ',n)			not found.


# #note:- index &find function is same. but when substring is not found then index give error
# #		 and find  give -1.



# s='universal informatic'
# n=s.rfind('i')
# print('found index: ',n)
# n=s.rfind('infor')			#return first character index number.
# print('found index: ',n)
# n=s.rfind('p')				#if substring is not found it will give return -1.
# print('found index: ',n)
# n=s.rfind('r',7)				#search after index number 7.
# print('found index: ',n)
# n=s.rfind('i',3,11)			#search between 3to 10index number.
# print('found index: ',n,'\n')



# s='universal informatic'
# n=s.rindex('l')
# print('found rindex: ',n)
# n=s.rindex('infor')			#return first character index number.
# print('found rindex: ',n)
# #n=s.rindex('p')				#if substring is not found it will give error.
# #print('found index: ',n)
# n=s.rindex('r',7)				#search after index number 7.
# print('found index: ',n,'')
# n=s.rindex('i',3,11)			#search between 3to 10index number.
# print('found index:',n,'\n')				


# #Note:-R find and R index function is searching substring from backward side but index number is counting
# #			from front side.



# s='universal informatic'
# print('actual string: ',s)
# s=s.encode('utf-8')				#encoding
# print('encoded string: ',s)
# s=s.decode('utf-8')				#decoding
# print('decoded string: ',s)


# #count method
# s='universal informatic'
# print('string is : ',s)
# n=s.count('i')				#total number of i in string.
# print('total number: ',n)


# #copy method --> not support string
# s='universal'
# print(s)
# print('id of t',id(s))
# t=s						#in this type copy data store in same reference id.
# print(t)
# print('id of t',id(t))
# '''t=s.copy()					#in this type copy data store in deferent reference id.
# print(t)
# print('id of t',id(t))''' #not support for string
# #