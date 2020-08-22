#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python37-32/python.exe
print("Content-type:text/html")
print("")

import M_conn,cgitb

cgitb.enable()
 
db=M_conn.dbconfig()
cursor=db.cursor()
form=M_conn.cgiconfig()

s=form.getvalue('s')
	
if s!=None:
	email=form.getvalue('email')
	op=form.getvalue('op')
	cnp=form.getvalue('cnp')
	query="update registration set passw='%s' where email='%s' && passw='%s'" %(cnp,email,op) 
	res=cursor.execute(query)
	db.commit()
	if res==1:
		print("<script> alert('password changed successfully')</script><script> window.location='loginpage.py'</script>")
	else:
		print("<script> alert('password not changed successfully')</script>")
	
fp=open('@headcode.py','r')
data=fp.read()
print(data)
fp.close()

fp=open('@usernav.py','r')
data=fp.read()
print(data)
fp.close()



		
		
		
print("""

<br clear="all">
<center>	<div class="cng" >
	 
	 

	<form  method="GET" action="">
			<br>
             <center>  <h3>Change passward<h3>  </center>
			   <br>
			
				<table >
				<tr>
						<td>Email or username</td>
						<td><input type="text" name="email" /></td>
					</tr>
					<tr>
						<td>Old passward: </td>
						<td><input type="password" name="op"/></td>
					</tr>
					<tr>
						<td>New Password: </td>
						<td><input type="password" name="np"/></td>
					</tr>
					
					<tr>
						<td> Conform New Password: </td>
						<td><input type="password" name="cnp"/></td>
					</tr>
						
				</table>
				<center><br><input type="submit" name="s" value="Change passward"/><center>
				</form>
				

                
			</div></center>

""")



fp=open('@footer.py','r')
data=fp.read()
print(data)
fp.close()

