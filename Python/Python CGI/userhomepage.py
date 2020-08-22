#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python37-32/python.exe
print("Content-type:text/html")
print("")


import M_usertracker,cgitb
cgitb.enable()
if M_usertracker.usercheck():
	print("<script>alert('IP tracking, Invalid user login first')</script>")
	print("<script>window.location='loginpage.py'</script>")
	
d=M_usertracker.userdetails_nm()


fp=open('@headcode.py','r')
data=fp.read()
print(data)
fp.close()


fp=open('@usernav.py','r')
data=fp.read()
print(data)
fp.close()





fp=open('@header.py','r')
data=fp.read()
print(data)
fp.close()

fp=open('@marque.py','r')
data=fp.read()
print(data)
fp.close()


fp=open('@slider.py','r')
data=fp.read()
print(data)
fp.close()

print("welcome,",d)


fp=open('@footer.py','r')
data=fp.read()
print(data)
fp.close()



