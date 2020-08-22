#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python37-32/python.exe
print("Content-type:text/html")
print("")

import M_conn,cgitb
cgitb.enable()
db=M_conn.dbconfig()
cursor=db.cursor()
form=M_conn.cgiconfig()

	
blockpid=form.getvalue('block')
if blockpid!=None:
	query="update adpost set vstatus='0' where pid=%s" %(blockpid)
	cursor.execute(query)
	db.commit()
	print("<script>alert('Post blocked')</script>")
	print("<script>window.location='managepostadminpage.py'</script>")

	
	
unblockpid=form.getvalue('unblock')
if unblockpid!=None:
	query="update adpost set vstatus='1' where pid=%s" %(unblockpid)
	cursor.execute(query)
	db.commit()
	print("<script>alert('Post unblocked')</script>")
	print("<script>window.location='managepostadminpage.py'</script>")
	
delpid=form.getvalue('del')
if delpid!=None:
	query="delete from adpost where pid=%s" %(delpid)
	cursor.execute(query)
	db.commit()
	print("<script>alert('Post Deleted')</script>")
	print("<script>window.location='managepostadminpage.py'</script>")
	
	
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



query="select * from adpost"
cursor.execute(query)
data=cursor.fetchall()


print("""
   <br clear="all">
<center>
<h2 >View All Ads list</h2>
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
 <th>Title</th>
 <th>Description</th>
 <th>Price</th>
 <th>Image1</th>
 <th>Image2</th>
 <th>Image3</th>
 <th>Address</th>
 <th>Email</th>
 <th>Block/Un-block</th>
 <th>Action</th>	
</tr>
""")




for row in data:
	print("<tr>")
	print("<td colspan='10' ><hr><td>")
	print("</tr>")
	print("<tr>")
	print("<td>",row[1],"</td>")
	print("<td>",row[3],"</td>")
	print("<td>",row[4],"</td>")
	print("<td><img src='uploads/"+row[5]+"' width='70px'/></td>")
	print("<td><img src='uploads/"+row[6]+"' width='70px'/></td>")
	print("<td><img src='uploads/"+row[7]+"' width='70px'/></td>")
	print("<td>",row[8],"</td>")
	print("<td>",row[9],"</td>")
	if row[12]==0:
		print("<td><a title='unblock Post' href='managepostadminpage.py?unblock="+str(row[0])+"'><img src='images/unblock.png' height='30' width='40'/></a></td>")
	else: 
		print("<td><a title='block Post' href='managepostadminpage.py?block="+str(row[0])+"'><img src='images/block.png' height='30' width='40'/></a></td>")
	print("<td><a title='Delete Post' href='managepostadminpage.py?del="+str(row[0])+"'><img src='images/delete.png' height='30' width='80'/></a></td>")
	print("</tr>")

	
	
print("""	
		</table>			
			
		</div></center>
		""")
	

fp=open('@footer.py','r')
data=fp.read()
print(data)
fp.close()	


