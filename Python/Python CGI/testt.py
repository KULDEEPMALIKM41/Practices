		import smtplib
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login("kuldeepmalikm41@gmail.com", "k1u2l3d4e5#1")
		msg = """Welcome to PostKrde.com
		
		You have successfully registered ,your login 
credintials


Username : """+email+"""
password : """+passw+"""

Click on below link to verify account

http://localhost/pythonproject/verifypage.py?email="""+email+"""               

		""" 
		server.sendmail("kuldeepmalikm41@gmail.com",email,msg)
		print("<script>alert('Register successfully, Verify your account from INBOX')</script>")
		print("<script>alert(window.location='loginpage.py')</script>")
	else:	
		print("<script>alert('Registration failed')</script>")