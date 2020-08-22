#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python37-32/python.exe
print("Content-type:text/html")
print("")

fp=open('@headcode.py','r')
data=fp.read()
print(data)
fp.close()

import M_usertracker,cgitb,M_conn
cgitb.enable()

form=M_conn.cgiconfig()
pid=form.getvalue('pid')
print(pid)
db=M_conn.dbconfig()
cursor=db.cursor()
query="select * from adpost where pid=%s" %(pid)
cursor.execute(query)
data=cursor.fetchone()

if M_usertracker.usercheck():
	print("<script>alert('IP tracking, Invalid user login first')</script>")
	print("<script>window.location='loginpage.py'</script>")
d=M_usertracker.userdetails_eml()

print("""
<body>
<div >
		  <center>
""")




#Set useful variables for paypal form
paypalURL = 'https://www.sandbox.paypal.com/cgi-bin/webscr' 
#Test PayPal API URL

paypalID = 'kmaliseller@gmail.com'
#Business Email



amount=data[4]
uid=d
pname=''
print("""
    <img src='uploads/"""+data[5]+"""' height='100' width='200'/>
    <br>
    Name: """+data[1]+"""
    <br>
    Price: """+data[4]+"""
    <form action='"""+paypalURL+"""' method="get">
        <!-- Identify your business so that you can collect the payments. -->
        <input type="hidden" name="business" value='"""+paypalID+"""'>
        
        <!-- Specify a Buy Now button. -->
        <input type="hidden" name="cmd" value="_xclick">
        
        <!-- Specify details about the item that buyers will purchase. -->
        <input type="hidden" name="pid" value='"""+pid+"""'>
        <input type="hidden" name="item_name" value='"""+pname+"""'>
        <input type="hidden" name="item_number" value="1">
        <input type="hidden" name="amount" value='"""+amount+"""'>
        <input type="hidden" name="currency_code" value="USD">
        
        <!-- Specify URLs -->
        <input type='hidden' name='cancel_return' value='http://localhost/pythonproject/cancelpage.py'>
        <input type='hidden' name='return' value='http://localhost/pythonproject/successpage.py?pid="""+pid+"""&uid="""+uid+"""&amount="""+amount+"""'>
        
        <!-- Display the payment button. -->
        <input type="image" name="submit" border="0"
        src="https://www.paypalobjects.com/en_US/i/btn/btn_buynow_LG.gif" alt="PayPal - The safer, easier way to pay online">
        <img alt="" border="0" width="1" height="1" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" >
    </form>
""")