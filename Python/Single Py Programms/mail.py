import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("kuldeepmalikm41@gmail.com", "k1u2l3d4e5#1")
msg = """Welcome to PostKrde.com""" 
server.sendmail("kuldeepmalikm41@gmail.com",'bharatpatidar5429@gmail.com',msg)
print("Register successfully")