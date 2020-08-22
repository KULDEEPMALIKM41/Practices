#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python37-32/python.exe
print("Content-type:text/html")
print("")

fp=open('@headcode.py','r')
data=fp.read()
print(data)
fp.close()

fp=open('@nav.py','r')
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

import M_conn,cgitb
cgitb.enable()
form=M_conn.cgiconfig()
db=M_conn.dbconfig()
cursor=db.cursor()
scatnm=form.getvalue('scatnm')
catnm=form.getvalue('catnm')
query1="select * from adcat order by catid desc"
cursor.execute(query1)
data1=cursor.fetchall()
query="select * from adpost where scat_nm='"+scatnm+"'order by pid desc"
cursor.execute(query)
data=cursor.fetchall()

print("""



<style>



#scat
{
	padding-left:72px;
	height:AUTO;
	width:64.95%;
	float:left;
}	
	


#cat
{
	float:left;
	MARGIN-LEFT:20PX;
	PADDING-LEFT:100PX;
	height: auto;
	width:420px;
}

</style>
<div>	

<div  id='scat' ><h3 align="left" style="color:purple; font-family:times new roman;" >"""+catnm+"""-->>"""+scatnm+"""-->></h3><br><br>

		""")
for row in data:
		print("""<a href='fulladspage.py?scatnm="""+scatnm+"""&pid="""+str(row[0])+"""&catnm="""+catnm+"""'>
				<div style="border:2px solid blue; width:700px;border-radius:20px">
				<table cellspacing='30' style=" width:700px; height:150px;">
<tr>
<td rowspan='3' width=40%'>
<center>
<img style="margin-top:10px;" src='uploads/"""+row[5]+"""' height='100' width='150' /> 
</center>
</td>
<td><b>Title : """+row[1]+"""</b></td>
</tr>
<tr>
<td><b>Description : """+row[3]+"""</b></td>
</tr>
<tr>
<td><b>Price : """+row[4]+"""</b></td>
</tr>
<tr>
<td></td>



</tr>
</table></div></a>
<br><br>			
		""")

print("""</div>




	<div id="cat">
				<h1 style="color:orange;"> Category </h1>
			<br><ul>""")
for row1 in data1:
		print("""<font size="3px" ><li><a href='viewscatpage.py?catnm="""+row1[1]+"""' style="color: #660033;">"""+row1[1]+"""</a></li><br>""")
			
print("""</ul></font>
	</div>	
</div>

<br clear="all">
""")
				
				
				
				
				

fp=open('@footer.py','r')
data=fp.read()
print(data)
fp.close()