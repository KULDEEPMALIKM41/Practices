a = input('Enter height :- ')
b = input('Enter width :- ')
if '.' in a:
  x1,x2 = a.split('.')
else:
  x1,x2 = int(a), 0

if '.' in b:
  y1,y2 = b.split('.')
else:
  y1,y2 = int(b), 0

a = float(x1)+float(int(x2)/12)
b = float(y1)+float(int(y2)/12)

print(a*b)