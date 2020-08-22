try: 
	from googlesearch import search
except ImportError: 
	print("No module named 'google' found") 

# to search 
query = "fb-Kuldeep.Mali.Gorpad"

for j in search(query,  num=10, stop=2, pause=2):
	print(j) 

