import bisect
value = 4
list1 = [1,2,3,4,8,6,12] #bisect work only sorted list.
print(list1)

#get list1 index number using bisect for insert value and list1 keep make sort.
print(bisect.bisect(list1, value))
print(bisect.bisect_left(list1, value))
print(bisect.bisect_right(list1, value))

#update list1 with value and keep sort using bisect.
bisect.insort(list1, value)
print(list1)

