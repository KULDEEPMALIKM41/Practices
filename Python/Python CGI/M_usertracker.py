import os

def userdetails_eml():
	if 'HTTP_COOKIE' in os.environ:
		cdata=os.environ['HTTP_COOKIE']
		clist=cdata.split(';')
		(cnm,cval)=clist[2].split('=')	 
		return cval
		
def userdetails_nm():
	if 'HTTP_COOKIE' in os.environ:
		cdata=os.environ['HTTP_COOKIE']
		clist=cdata.split(';')
		(cnm,cval)=clist[0].split('=')	
		return cval
		
def usercheck():
	if 'HTTP_COOKIE' in os.environ:
		cdata=os.environ['HTTP_COOKIE']
		clist=cdata.split(';')
		(cnm,cval)=clist[1].split('=')
		if cval=="user":
			return False
		else:
			return True	
	else:
		return True
		
def admincheck():
	if 'HTTP_COOKIE' in os.environ:
		cdata=os.environ['HTTP_COOKIE']
		clist=cdata.split(';')
		(cnm,cval)=clist[1].split('=')
		if cval=="admin":
			return False
		else:
			return True	
	else:
		return True	