a = 'bcacacacacac'

def count_substring(string,substr):
	count1 = 0
	for i in range(len(string)-len(substr)+1):
		if string[i:i+len(substr)] == substr:
			count1+=1
	count2 = string.count(substr)
	return count1,count2

print(count_substring(a,'aca'))