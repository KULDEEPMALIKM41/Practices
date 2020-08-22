#calendar module -->

import calendar
import time

"""epoch=time.time()
print('secs : ',epoch)

gmtime=time.gmtime(epoch)         #GMT time
print('gmtime : ',gmtime)

d=calendar.timegm(gmtime) #inverse of time.gmtime
print(d)"""

d=calendar.month(1998,10,w=2,l=1)				#return one month
print(d)

d=calendar.calendar(2019)	#return all month of year.
print(d)

d=calendar.weekday(2018,7,4)	#return week day 0-6, 0-Monday to 6-Sunday
print(d)

d=calendar.firstweekday()		# first week day, by default 0-Monday
print(d)

d=calendar.isleap(2020)     #if leap year return true otherwise false
print(d)

d=calendar.leapdays(0,2021) #count leap days 
print(d)
"""

d=calendar.monthcalendar(2018,7) #month in list format.
print(d)

d=calendar.monthrange(2018,12)  # return month starting day & total days in month
print(d)

d=calendar.setfirstweekday(6)	#???????
print(d)

d=calendar.prmonth(2018,5,w=2,l=1)	#return one month	
print(d)

d=calendar.prcal(2019,w=2,l=1,c=6)	#return all month of year.
print(d)


"""






