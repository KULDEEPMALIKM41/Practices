#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python37-32/python.exe
print("Content-type:text/html")
print("")

import M_usertracker,cgitb
cgitb.enable()
if M_usertracker.admincheck():
	print("<script>alert('IP tracking, Invalid user login first')</script>")
	print("<script>window.location='loginpage.py'</script>")
	
d=M_usertracker.userdetails_eml()

fp=open('@headcode.py','r')
data=fp.read()
print(data)
fp.close()


fp=open('@adminnav.py','r')
data=fp.read()
print(data)
fp.close()




fp=open('@adminmarque.py','r')
data=fp.read()
print(data)
fp.close()


fp=open('@footer.py','r')
data=fp.read()
print(data)
fp.close()	
