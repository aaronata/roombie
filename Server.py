import socket
import threading
import time


class Server(threading.Thread):


	def __init__(self,port,queue):
		super(Server,self).__init__()
		self.port = port
		self.queue = queue
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	def run(self):
		self.sock.bind(('',self.port))
		self.sock.listen(1)
		while(True):

			try:
				self.con,addr = self.sock.accept()
				print("Connection from " + str(addr))
				while 1:
					data = self.con.recv(1024)
					
					if(data ==""):
						continue
					if(data is None):
						break
					self.queue.put(data)
			except RuntimeError as e:
				pass

	def close(self):
		self.sock.close()


if __name__ == "__main__":
	s = Server(port=5000,queue=None)
	s.start()
	s.join()
