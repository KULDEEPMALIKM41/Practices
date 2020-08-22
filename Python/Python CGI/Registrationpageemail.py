#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python37-32/python.exe
print("Content-type:text/html")
print("")


import cgi,cgitb,time,pymysql

cgitb.enable()

db=pymysql.connect('localhost','root','','kuldeep')
cursor=db.cursor()
form=cgi.FieldStorage()


s=form.getvalue('s')
if s!=None:
	nm=form.getvalue('nm')
	email=form.getvalue('email')
	passw=form.getvalue('pass')
	address=form.getvalue('address')
	mob=form.getvalue('mob')
	
	city=form.getvalue('city')
	gender=form.getvalue('gender')
	ctime=time.strftime('%d-%m-%Y,%H:%M:%S')
	
	query="insert into registration values(Null,'%s','%s','%s','%s','%s','%s','%s',0,'user','%s')" %(nm,email,passw,address,city,mob,gender,ctime)
	
	result=cursor.execute(query)
	#db.commit()
	
	if result:
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
	

		
		
fp=open('@headcode.py','r')
data=fp.read()
print(data)
fp.close()

fp=open('@nav.py','r')
data=fp.read()
print(data)
fp.close()

print("""

<br clear="all">
<center>	<div class="regi" >
	 
	 

	<form  method="post" action="">
			<br>
             <center>  <h3> Register here!!!<h3>  </center>
			   <br>
			
				<table	>
					<tr>
						<td>Name:</td>
						<td><input type="text" name="nm"/></td>
					</tr>
					<tr>
						<td>Email Id or Username: </td>
						<td><input type="text" name="email"/></td>
					</tr>
					<tr>
						<td>Password: </td>
						<td><input type="password" name="pass"/></td>
					</tr>
					<tr>
						<td>Address: </td>
						<td><textarea rows="5" cols="26" name="address"></textarea></td>
					</tr>
					<tr>
						<td>Phone No.: </td>
						<td><input type="text" name="mob"/></td>
					</tr>
					<tr>
						<td>City: </td>
						<td>
							<select style="width:220px;" name="city">
								<option>Select city</option>
								<option>Indore</option>
								<option>Bhopal</option>
								<option>Ujjain</option>	
							</select>
						</td>
					</tr>
					<tr>
						<td>Gender: </td>
						<td>
						<input type="radio" name="gender" value="male"/>
						 Male
						&nbsp;&nbsp;&nbsp;
						<input type="radio" name="gender" value="female"/>
						 Female
						</td>
					</tr>	
				</table>
				<center><br><input type="submit" name="s" value="Register"/><center>
				</form>
				

                
			</div></center>


""")
fp=open('@footer.py','r')
data=fp.read()
print(data)
fp.close()

	
		