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
	catnm=form.getvalue('catnm')
	caticn=form['caticn']
	ofn=caticn.filename
	fn=str(time.time())+'-'+ofn
	fp=open('uploads/'+fn,'wb')
	fp.write(caticn.value)
	#fp.write(caticn.file.read())
	fp.close()
	query="insert into adcat value (Null,'%s','%s')"%(catnm,fn)
	result=cursor.execute(query)
	db.commit()
	if result:
		print("<script>alert('category added')</script>")
	else:
		print("<script>alert('Category not added')</script>")
	

fp=open('@headcode.py','r')
data=fp.read()
print(data)
fp.close()

fp=open('@adminnav.py','r')
data=fp.read()
print(data)
fp.close()

print("""
<br clear="all">
<center>	<div class="adcat" >
	 <form  method="POST" enctype='multipart/form-data' action="">
			<br>
             <center>  <h3> Add Category<h3>  </center>
			   
			
				<table >
				
					<tr>
						<td>Category Name</td>
						<td><input type="text" name="catnm"/></td>
					</tr>
					<tr>
						<td>Category Icon</td>
						<td><input type="file" name="caticn"/></td>
					</tr>
						
				</table>
				<center><br><input type="submit" name="s" value="Add Category"/><center>
				</form>
		</div></center>


""")
		

fp=open('@footer.py','r')
data=fp.read()
print(data)
fp.close()	

