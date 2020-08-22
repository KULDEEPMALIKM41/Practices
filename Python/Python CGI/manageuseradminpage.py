#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python37-32/python.exe
print("Content-type:text/html")
print("")

import M_conn,cgitb
cgitb.enable()
db=M_conn.dbconfig()
cursor=db.cursor()
form=M_conn.cgiconfig()

	
blockregid=form.getvalue('block')
if blockregid!=None:
	query="update registration set vstatus='0' where rid=%s" %(blockregid)
	cursor.execute(query)
	db.commit()
	print("<script>alert('User blocked')</script>")
	print("<script>window.location='manageuseradminpage.py'</script>")

	
	
unblockregid=form.getvalue('unblock')
if unblockregid!=None:
	query="update registration set vstatus='1' where rid=%s" %(unblockregid)
	cursor.execute(query)
	db.commit()
	name=form.getvalue('name')
	print("<script>alert('User unblocked')</script>")
	print("<script>window.location='manageuseradminpage.py'</script>")
	
delregid=form.getvalue('del')
if delregid!=None:
	query="delete from registration where rid=%s" %(delregid)
	cursor.execute(query)
	db.commit()
	print("<script>alert('User Deleted')</script>")
	print("<script>window.location='manageuseradminpage.py'</script>")
	
	
fp=open('@headcode.py','r')
data=fp.read()
print(data)
fp.close()



fp=open('@adminnav.py','r')
data=fp.read()
print(data)
fp.close()




fp=open('@adminmarque.py','r')
data=fp.read()
print(data)
fp.close()



query="select * from registration where regrol='user'"
cursor.execute(query)
data=cursor.fetchall()


print("""
   <br clear="all">
<center>
<h2 >View All users list</h2>
<div  style=" background:lightpink; margin-top:15px; height:auto; width:1345px; border:1px solid black" >
<br>

<style>
table, th, td
{
	text-align: center;
}
</style>
<table style="width:1250px;margin-bottom:20px;">
<tr>
<th>RegID</th> 
<th>Name</th>
<center><th>Email</th> 
<center><th>Address</th> 
<th>City</th> 
<th>Mobile</th> 
<th>Gender</th>
<th>Block/Un-block</th>
<th>Action</th>
</tr>
""")




for row in data:
	print("<tr>")
	print("<td colspan='9' ><hr><td>")
	print("</tr>")
	print("<tr>")
	print("<td>",row[0],"</td>")
	print("<td>",row[1],"</td>")
	print("<td>",row[2],"</td>")
	print("<td>",row[4],"</td>")
	print("<td>",row[5],"</td>")
	print("<td>",row[6],"</td>")
	print("<td>",row[7],"</td>")
	if row[8]=='0':
		print("<td><a title='unblock User' href='manageuseradminpage.py?unblock="+str(row[0])+"'><img src='images/unblock.png' height='30' width='40'/></a></td>")
	else: 
		print("<td><a title='block User' href='manageuseradminpage.py?block="+str(row[0])+"'><img src='images/block.png' height='30' width='40'/></a></td>")
	print("<td><a title='Delete User' href='manageuseradminpage.py?del="+str(row[0])+"'><img src='images/delete.png' height='30' width='80'/></a></td>")
	print("</tr>")

	
	
print("""	
		</table>			
			
		</div></center>
		""")
	

fp=open('@footer.py','r')
data=fp.read()
print(data)
fp.close()	


