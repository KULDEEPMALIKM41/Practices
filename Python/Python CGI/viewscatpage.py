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
catnm=form.getvalue('catnm')
query1="select * from adcat order by catid desc"
cursor.execute(query1)
data1=cursor.fetchall()
query="select * from adsubcat where cat='"+catnm+"'order by scatid desc"
cursor.execute(query)
data=cursor.fetchall()

print("""



<style>

#cntr
{
	PADDING:10PX;
	height:325PX;
	width:1345px;
	
}

#scat
{
	height:AUTO;
	width:64.95%;
	float:left;
}	
	
#catmain
{
	float:left;
	margin:7px;
	height: 100px;
	width:125px;
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

<div id="cntr">
		<div  id='scat' ><h3 align="left" style="color:purple; font-family:times new roman;" >"""+catnm+"""-->></h3><br>
""")
for row in data:
		print("""<a href='viewadspage.py?scatnm="""+row[1]+"""&catnm="""+catnm+"""'><div id="catmain">
				<center><img src='uploads/"""+row[2]+"""' height='70' width='50'>
				<br>
				<b style="color: #336699">"""+row[1]+"""</b></center>
	
			</div>				
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