# Method 1; Work fine for n length string; Complex method but very fast.
def isAdjacent(string):
	'''isAdjancent function made for handle string type value
		and return rearrange posible result
		input type - String(set of charters), e.g.- ssa , sas'''
	string = string.strip().replace(" ","") # Remove all whitespaces
	str_list = list(string) # Convert python string to list
	char_freq=dict((char,str_list.count(char)) for char in str_list) # Get frequency of char with python dict type
	if (len(string)+1)//2 >= max(char_freq.values()):
		# Increase string length to 1 and set floor 2 and it is compare by maximax character frequency value
		result = [None]*len(string) # Set multiple null value as string length
		sorted_list = []  # define sorted_list python list variable
		sort_dict = dict(sorted(char_freq.items(),key=lambda x:x[1], reverse=True)) # Sorting dict value
		for key in sort_dict: sorted_list+=[key]*sort_dict[key] # distribute sorted list value with order

		# In this section handle string to rearange format and return result
		flage,insert_val = 0,0 # Set initial flage and insert_val variable assign with 0
		while flage < len(string): result[flage] = sorted_list[insert_val]; flage += 2; insert_val += 1 # Set while loop and arrange sorted_list
		flage = 1
		while flage < len(string):result[flage] = sorted_list[insert_val]; flage += 2; insert_val += 1 # Set While loop for rearrange string value with list type of result
		return ''.join(result)
	else:
		return None

print(isAdjacent('kkuullddeepp'))


# Method 2; Work fine for only lessthan 10 char. string; Simple method but very slow.
from itertools import permutations
def isAdjacent(string):
	string = string.strip().replace(" ", "")  # Remove all whitespaces
	str_list = list(string) # Convert string to list
	if (len(string)+1)//2 < max([str_list.count(char) for char in str_list]):return None
	for perms in permutations(str_list):
		for index, ele in enumerate(perms):
			if index == len(perms)-1: return ''.join(perms)	elif ele == perms[index + 1]: break

print(isAdjacent('mmaallii'))