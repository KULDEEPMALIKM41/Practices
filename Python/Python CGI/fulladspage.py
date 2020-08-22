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


import M_conn,cgitb
cgitb.enable()
form=M_conn.cgiconfig()
db=M_conn.dbconfig()
cursor=db.cursor()
scatnm=form.getvalue('scatnm')
catnm=form.getvalue('catnm')
pid=form.getvalue('pid')
query1="select * from adcat order by catid desc"
cursor.execute(query1)
data1=cursor.fetchall()
query="select * from adpost where scat_nm='"+scatnm+"'order by pid desc"
cursor.execute(query)
data=cursor.fetchall()
query2="select * from adpost where pid="+pid+""
cursor.execute(query2)
data2=cursor.fetchone()

print("""

<div style="height:527px; width:1348px;">


<div style="height:525px; width:925px; border:1px solid black; float:left;">


<div class="container">
 
  <div class="show" href='uploads/"""+data2[5]+"""'>
    <img src='uploads/"""+data2[5]+"""' id="show-img">
  </div>
  <div class="small-img">
    <img src="images/online_icon_right@2x.png" class="icon-left" alt="" id="prev-img">
    <div class="small-container">
      <div id="small-img-roll">
        <img src='uploads/"""+data2[5]+"""' class='show-small-img' alt=''>
        <img src='uploads/"""+data2[6]+"""' class='show-small-img' alt=''>
        <img src='uploads/"""+data2[7]+"""' class='show-small-img' alt=''>
        
      </div>
    </div>
    <img src="images/online_icon_right@2x.png" class="icon-right" alt="" id="next-img">
  </div>
</div>
  <script src="js/jquery-3.3.1.min.js" integrity="sha384-tsQFqpEReu7ZLhBV2VZlAu7zcOV+rXbYlF2cqB8txI/8aZajjp4Bqd+V6D5IgvKT" crossorigin="anonymous"></script>
  <script src="js/zoom-image.js"></script>
  <script src="js/main.js"></script>
	
	
	
	
	
	</div >
	
<div style="border: 1px solid green; height:525px; width: 422px; float:left;">


<table style="margin-left:7px; margin-top:5px; width:420px; height:400px;">
	<tr>
	<td>Title<td>	
	<td>:  """+data2[1]+"""<td>	
	<tr>
	
	<tr>
	<td>Description<td>	
	<td> : """+data2[3]+"""<td>	
	<tr>
	
	
	<tr>
	<td>Price<td>	
	<td> : """+data2[4]+"""<td>	
	<tr>
	
	
	<tr>
	<td>Address<td>	
	<td> : """+data2[8]+"""<td>	
	<tr>
	
	
	<tr>
	<td>Email<td>	
	<td>:  """+data2[9]+"""<td>	
	<tr>
	
	<tr>
	<td>Mobile No<td>	
	<td>:  """+data2[10]+"""<td>	
	<tr>
	
	<tr>
	<td>City<td>	
	<td>:  """+data2[11]+"""<td>	
	<tr>





</table>

<br>

<a href='loginpaypage.py?pid="""+str(data2[0])+"""'><center><button style="background-color: #4CAF50; border: none; color: white; padding: 15px 32px;text-align: center;font-size: 16px;">Buy Now</button></center></a>

</div>


<br clear="all">

</div>


""")

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