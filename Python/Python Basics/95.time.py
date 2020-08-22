#time module

import time

t=time.altzone #?????
print(t)

epoch=time.time()
print('secs : ',epoch)

timetup=time.localtime(epoch)		#IST time
print('time tup : ',timetup)

usabletime=time.asctime(timetup)
print('usabletime : ',usabletime)

gmtime=time.gmtime(epoch)         #GMT time
print('gmtime : ',gmtime)

usabletime=time.asctime(gmtime)
print('usabletime : ',usabletime,'\n\n\n')


import time
t=time.strftime('%a')	#day name
print(t,'\n')

t=time.strftime('%A')	#day full name
print(t,'\n')

t=time.strftime('%b')	#month name
print(t,'\n')

t=time.strftime('%B')	#month full name
print(t,'\n')

t=time.strftime('%c')	#usable time "time.asctime(timetup)"
print(t,'\n')

t=time.strftime('%d')	#current month date
print(t,'\n')

t=time.strftime('%D')	#current : dd/mm/yy
print(t,'\n')

t=time.strftime('%m')	#current month
print(t,'\n')

t=time.strftime('%M')	# current minute
print(t,'\n')

t=time.strftime('%h')	#month name
print(t,'\n')


t=time.strftime('%H')	#hour in 24 format
print(t,'\n')

t=time.strftime('%I')	#hour in 12 format
print(t,'\n')

t=time.strftime('%S')	#current second
print(t,'\n')

t=time.strftime('%y')	#current year-18
print(t,'\n')

t=time.strftime('%Y')	#current year-2018
print(t,'\n')

t=time.strftime('%d/%m/%Y   %I-%M-%S')	#current second
print(t,'\n')

