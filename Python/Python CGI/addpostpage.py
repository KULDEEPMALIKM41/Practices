#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python37-32/python.exe
print("Content-type:text/html")
print("")


import M_conn,cgitb,time
cgitb.enable()
form=M_conn.cgiconfig()
db=M_conn.dbconfig()
cursor=db.cursor()

s=form.getvalue('s')
if s!=None:
	title=form.getvalue('title')
	scat_nm=form.getvalue('scat_nm')
	description=form.getvalue('description')
	price=form.getvalue('price')
	address=form.getvalue('address')
	email=form.getvalue('email')
	mob=form.getvalue('mob')
	city=form.getvalue('city')
	

	myimg1=form['myimg1']
	myimg1v=myimg1.value
	
	if len(myimg1v)>0:
		ofn1=myimg1.filename
		fn1=str(time.time())+'-'+ofn1
		fp=open('uploads/'+fn1,'wb')
		fp.write(myimg1v)
		fp.close()
	else:
		fn1="dummy.png"
	
		
	myimg2=form['myimg2']
	myimg2v=myimg2.value
	if len(myimg2v)>0:
		ofn2=myimg2.filename
		fn2=str(time.time())+'-'+ofn2
		fp=open('uploads/'+fn2,'wb')
		fp.write(myimg2v)
		fp.close()
	else:
		fn2="dummy.png"	

		
	myimg3=form['myimg3']
	myimg3v=myimg3.value
	if len(myimg3v)>0:
		ofn3=myimg3.filename
		fn3=str(time.time())+'-'+ofn3
		fp=open('uploads/'+fn3,'wb')
		fp.write(myimg3v)
		fp.close()
	else:
		fn3="dummy.png"
		
		
	query="insert into adpost values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',0,0)" %(title,scat_nm,description,price,fn1,fn2,fn3,address,email,mob,city)

	result=cursor.execute(query)
	db.commit()
	if result:
		print("<script>alert('post added')</script>")
	else:
		print("<script>alert('post not added')</script>")








query="select scatnm from adsubcat"
cursor.execute(query)
data1=cursor.fetchall()


		
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
<center>	<div class="adpost" >
	 
	 

	<form method="POST" enctype='multipart/form-data' action="">
			<br>
             <center>  <h3>Post Your Ads Here!!!<h3>  </center>
			   <br>
			
				<table	>
					<tr>
						<td>Title :</td>
						<td><input type="text" name="title"/></td>
					</tr>
					<tr>
						<td>Category : </td>
						<td><select name="scat_nm" ><option>---Select Category---</option>""")
for row in data1:
	print("<option>",row[0],"</option>")
					
					
print("""
</select>
</td>
</tr>
					<tr>
						<td>Ads Description : </td>
						<td><textarea rows="4" cols="26" name="description"></textarea></td>
					</tr>
					<tr>
						<td>Price : </td>
						<td><input type="text" name="price"/></td>
					</tr>
					<tr>
						<td>Ads Images: </td>
						<td>
							Select File : <input type="file" name="myimg1" />
						</td>
					</tr>
                                   
                      <tr>
							<td></td>
							<td>  Select File : <input type="file" name="myimg2" /></td>
					</tr>
                              
                     <tr>
							<td></td>
							<td> Select File : <input type="file" name="myimg3" /> </td>
					</tr>
						
					<tr>
						<td>Address : </td>
						<td><textarea rows="4" cols="26" name="address"></textarea></td>
					</tr>
					
					  <tr>
                                <td>Email ID</td>
                                <td>
                                <input type="text" name="email" />    
                                </td>
                            </tr>
                        <tr>
                            <td>Phone no.</td>
                            <td>
                            <input type="text" name="mob" />    
                            </td>
                        </tr>
                        <tr>
                            <td>City</td>
                            <td>
                            <select name="city">
                                <option>Select City</option>
                                <option>Indore</option>
                                <option>Bhopal</option>
                                <option>Ujjain</option>
                            </select>    
                            </td>
                        </tr>
					
				</table>
				<center><br><input type="submit" name="s" value="Add Post"/><center>
				</form>
				

                
			</div></center>


""")
fp=open('@footer.py','r')
data=fp.read()
print(data)
fp.close()

	
		