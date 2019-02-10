import threading
import create2api
import time

class Doomba(threading.Thread):
	def __init__(self,queue):
		super(Doomba,self).__init__()
		self.queue = queue
		self.bot = create2api.Create2()
		self.bot.start()
		self.bot.safe()

	def playSong(self):
		song = "C4L G4M E4M E4L D4M C4M C4M F4L E4M E4M D4M D4M C4L C4M G4M E4M E4M D4M D4M C4M C4M A3L G3L \
			pauseM C4M C4M G4M E4M E4M D4M D4M C4M C4M F4L E4M E4M D4M D4M C4L C4M G4M E4M E4M D4M D4M C4M C4M D4L A3L"
		self.bot.playFakeMidi(song)

	def stop(self):
		self.bot.drive_straight(0)
		
	def run(self):
		while(True):
			data = self.queue.get(True)
			print("Input: "+data)
			if data == "11":
				print("Foward")
				self.bot.drive_straight(200)
			elif data == "21":
				print("Right")
				self.bot.turn_clockwise(200)
			elif data == "31":
				print("Back")
				self.bot.drive_straight(-200)
			elif data == "41":
				print("Left")
				self.bot.turn_counter_clockwise(200)
			elif data == "5":
				self.bot.safe()
			elif data == "6":
				self.stop()
				self.playSong()
			else:
				self.stop()
			#self.bot.drive_straight(0)