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
	scatnm=form.getvalue('scatnm')
	cat=form.getvalue('cat')
	scaticn=form['scaticn']
	ofn=scaticn.filename
	fn=str(time.time())+'-'+ofn
	fp=open('uploads/'+fn,'wb')
	fp.write(scaticn.value)
	#fp.write(caticn.file.read())
	fp.close()
	query="insert into adsubcat value(Null,'%s','%s','%s')"%(scatnm,fn,cat)
	result=cursor.execute(query)
	db.commit()
	if result:
		print("<script>alert(' Sub category added')</script>")
	else:
		print("<script>alert('Sub Category not added')</script>")
	

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
             <center>  <h3> Add Sub Category<h3>  </center>
			   <br>
			
				<table >
				
					<tr>
						<td> Sub Category Name</td>
						<td><input type="text" name="scatnm"/></td>
					</tr>
					<tr>
						<td>Category</td>
						<td><select style="width:175px;" name='cat'><option>---select category---</option>""")

query="select catnm from adcat" 
cursor.execute(query)
data=cursor.fetchall()						
for row in data:						
	print("<option>",row[0],"</option>")					
						
print("""<select></td>
					</tr>
					<tr>
						<td> Sub Category Icon</td>
						<td><input type="file" name="scaticn"/></td>
					</tr>
					<tr>
				</table>
				<center><br><input type="submit" name="s" value="Add Sub Category"/><center>
				</form>
		</div></center>


""")
		

fp=open('@footer.py','r')
data=fp.read()
print(data)
fp.close()	

