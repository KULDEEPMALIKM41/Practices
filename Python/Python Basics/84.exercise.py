#tuple sort in descending order
t=(10,50,40,20,70,90,30,60,100,80)
print('after descinding',t)
t=list(t)
t.sort()
t.reverse()
t=tuple(t)
print('after descinding',t)