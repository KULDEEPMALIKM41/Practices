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

print("<center><h1>Contact page<h1></center>")

fp=open('@footer.py','r')
data=fp.read()
print(data)
fp.close()