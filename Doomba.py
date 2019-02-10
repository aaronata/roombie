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
		self.songs = [	"C4L G4M E4M E4L D4M C4M C4M F4L E4M E4M D4M D4M C4L C4M G4M E4M E4M D4M D4M C4M C4M A3L G3L pauseM C4M C4M G4M E4M E4M D4M D4M C4M C4M F4L E4M E4M D4M D4M C4L C4M G4M E4M E4M D4M D4M C4M C4M D4L A3L",
						"D#5L pauseS D#5M E5M pauseM B4M G#4S D#5L pauseS D#5M E5M pauseM B4M G#4S D#5L pauseS D#5M E5M pauseM B4M G#4S D#5L pauseS D#5M E5M pauseM B4M G#4S",
						"G#3S A#3S C#4S A#3S F4L F4L D#4L pauseM G#3S A#3S C4S G#3S D#4L D#4L C#4L pauseM  G#3S A#3S C#4S A#3S C#4L D#4M C4L A#3S G#3L pauseS G#3M D#4L C#4L",
						"G4L E4L C4L G3L A3M B3M C4M A3L C4M G3L pauseM D4L G4L E4L C4L D4L E4M D4L E4M D4L"]

	def playSong(self,number):
		song = self.songs[number]
		self.bot.playFakeMidi(song)
		if number == 0 :
			lyrics = "Somebody once told me the world is gonna roll me I ain't the sharpest tool in the shed    She was looking kind of dumb with her finger and her thumb In the shape of an 'L' on her forehead" 
			for i in range(len(lyrics)-4):
				self.bot.digit_led_ascii(lyrics[i:i+4])
				time.sleep(0.0735)

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
			elif data[0] == "6":
				self.stop()
				self.playSong(int(data[1:]))
			else:
				self.stop()
			#self.bot.drive_straight(0)