import queue as Queue
import socket
from threading import *
import datetime
import time
def worker():
	print ("in worker")
	item = q.get() # remove item from queue
	print (item)
	print ("task finished")
q = Queue.Queue()  # defining the Queue

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1111
print (host)
print (port)

serversocket.bind((host, port))

class client(Thread):

	def __init__(self, socket, address):
		Thread.__init__(self)
		self.sock = socket
		self.addr = address
		self.start()
	def run(self):
		while 1:
			st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
			print(self.sock.recv(1024).decode()+' sent @ '+ st + ':' , self.sock.recv(1024).decode())
			self.sock.send(b'Processing!')
			num_worker_threads = 5
			for i in range(num_worker_threads):
				t = Thread(target=worker)
				t.start()
			for item in range(num_worker_threads):
				q.put(item)  # put item in queue
serversocket.listen(5)
print ('server started and listening')
while 1:
	#clientsocket, address = serversocket.accept()
	client(serversocket.accept())






