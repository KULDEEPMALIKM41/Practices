#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python37-32/python.exe
print('Content-type:text/html')
print('')

import M_conn,cgitb
cgitb.enable()
db=M_conn.dbconfig()
cursor=db.cursor()

form=M_conn.cgiconfig()
unblockregid1=form.getvalue('email')
if unblockregid1!=None:
	query="update registration set vstatus='1' where email='%s'" %(unblockregid1)
	cursor.execute(query)
	db.commit()
	print("<script>alert('User Verified!!!')</script>")
	print("<script>window.location='loginpage.py'</script>")

mob=form.getvalue('mob')
chk=form.getvalue('chk')
otp=form.getvalue('otp')
otpemail=form.getvalue('otpemail')
	
if chk==otp and chk!=None:
	query="update registration set vstatus='1' where mob='%s' && email='%s'" %(mob,otpemail)
	res=cursor.execute(query)
	db.commit()
	if res:
		print("<script>alert('User Verified!!!')</script>")
		print("<script>window.location='loginpage.py'</script>")
	else:
		print("<script>alert('you are not valid user!!!')</script>")
		print("<script>window.location='otpverifypage.py'</script>")
	
	
if chk!=otp and chk!=None:
	print("<script>alert('OTP is not valid. Please try again')</script>")
	print("<script>window.location='otpverifypage.py?mob="+mob+"&email="+otpemail+"'</script>")

	

	