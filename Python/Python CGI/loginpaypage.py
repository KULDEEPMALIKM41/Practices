#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python37-32/python.exe


import M_conn,cgitb,http.cookies
cgitb.enable()

mycookie=http.cookies.SimpleCookie()


form=M_conn.cgiconfig()
db=M_conn.dbconfig()
cursor=db.cursor()

pid=form.getvalue('pid')

s=form.getvalue('s')

if s!=None:
	email=form.getvalue('email')
	passw=form.getvalue('pass')
	query="select * from registration where email='"+email+"' && passw='"+passw+"' && vstatus='1'"
	result=cursor.execute(query)
	if result:
		data=cursor.fetchone()
		
		mycookie['username']=email
		mycookie['role']=data[9]
		mycookie['name']=data[1]
		print(mycookie)

print("Content-type:text/html")
print("")

print(pid)
if s!=None:
	if result:
		print("<script>alert('Login Successfully')</script>")
		if data[9]=='admin':
			print("<script>window.location='adminhomepage.py'</script>")
		if data[9]=='user':
			print("""<script>window.location='userpaypage.py?pid="""+pid+"""'</script>""")
	else:
		print("<script>alert('Invalid user or verify your account from INBOX')</script>")

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
<center>	<div class="log" >
	 
	 

	<form  method="POST" action=''>
			<br>
             <center>  <h3> Login&Pay<h3>  </center>
			   <br>
			
				<table >
				
					<tr>
						<td>Email Id or Username: </td>
						<td><input type="text" name="email"/></td>
					</tr>
					<tr>
						<td>Password: </td>
						<td><input type="password" name="pass"/></td>
					</tr>
						
				</table>
				<center><br><input type="submit" name="s" value="Login"/><center>
				</form>
				

                
			</div></center>


""")

fp=open('@footer.py','r')
data=fp.read()
print(data)
fp.close()

