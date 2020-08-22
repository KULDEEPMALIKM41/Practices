#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python37-32/python.exe
print("Content-type:text/html")
print("")

import cgitb,M_conn
cgitb.enable()

form=M_conn.cgiconfig()
db=M_conn.dbconfig()
cursor=db.cursor()


pid = form.getvalue('pid')
uid = form.getvalue('uid') 
amount = form.getvalue('amount')


query="insert into payment values(NULL,'%s','%s','%s')" %(uid,pid,amount)

res=cursor.execute(query)
db.commit()

if res:
	print("<script>alert('Payment done')</script>")
	print("<script>window.location='Homepage.py'</script>")	
else:
	print("<script>alert('Payment failed')</script>")
	print("<script>window.location='Homepage.py'</script>")
