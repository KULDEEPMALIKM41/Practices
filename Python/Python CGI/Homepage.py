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


import M_conn
form=M_conn.cgiconfig()
db=M_conn.dbconfig()
cursor=db.cursor()
query="select * from adcat order by catid desc limit 0,12"
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

#cat
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

#sidebar
{
	float:left;
	MARGIN-LEFT:20PX;
	PADDING-LEFT:150PX;
	height: auto;
	width:420px;
}

</style>	
		
<div id="cntr">
		<div  id='cat' ><h2 align="left" style="color:purple; font-family:times new roman;" >Welcome to <span style="font-family:cursive; color:red; font-size:45px;">Post</span>Karde.com</h2><br>
""")
for row in data:
		print("""<a href='viewscatpage.py?catnm="""+row[1]+"""'><div id="catmain">
				<center><img src='uploads/"""+row[2]+"""' height='70' width='50'>
				<br>
				<b style="color: #336699">"""+row[1]+"""</b></center>
	
			</div>				
		""")

print("""</div>
	<div id="sidebar">
				<h1 style="color:orange;">Social Links</h1>
				<ul><br>
					<font size="5px" ><li><a href="#"  style="color: #C31AFF;">Facebook</a></li><br>
					<li><a href="#" style="color:#FF5733;">LinkedIn</a></li><br>
					<li><a href="#"  style="color:#660033;">Twitter</a></li><br>
					<li><a href="#" style="color:yellowgreen;">Our Blog</a></li>
				</ul></font>
	</div>	
</div>

<br clear="all">
""")	
				

fp=open('@footer.py','r')
data=fp.read()
print(data)
fp.close()