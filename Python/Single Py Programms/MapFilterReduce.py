list_demo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

def squre(n):
    return n**2

def is_divisable_by_3(n):
    if n%3 == 0:
        return True
    else:
        return False

def sum_elements(a,b):
    return a+b

squire_list = list(map(squre, list_demo))
print(squire_list)

divisable_by_3_list = list(filter(is_divisable_by_3, list_demo))
print(divisable_by_3_list)

from functools import reduce
sum = reduce(sum_elements, list_demo)
print(sum)