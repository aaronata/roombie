import sys
if sys.version[0]=='2':
	import Queue
else:
	import queue as Queue
import Server
import Doomba

if __name__ == "__main__":
	queue = Queue.Queue()
	port = 5000
	s = Server.Server(port,queue)
	d = Doomba.Doomba(queue)
	s.start()
	d.start()
	d.join()
	s.join()
