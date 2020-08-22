#help of way2sms

import zerosms
import getpass
import request
def zerosmssend():
	user_name=getpass.getpass("Enter username: ")
	user_pass=getpass.getpass("Enter userpass: ")
	msg=input("Mesage: ")
	send_to=getpass.getpass("Send to: ")
	zerosms.sms(user_name,user_pass,msg,send_to)
zerosmssend()