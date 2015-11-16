			# write a text into a file in background using thread
import threading
import time

class Back(threading.Thread):
	def __init__(self,text,file):
		threading.Thread.__init__(self)		#create a thread
		self.text = text
		self.file = file
		
	def run(self):		# run is a default function that is called when we start a thread
		print "Background task started."
		f = open(self.file, 'a')
		f.write(self.text + '\n')
		f.close()
		time.sleep(5)
		print "finished  background file writing in :",self.file
		
text = raw_input("Enter the text to be written in file:\t")
file = raw_input("Enter the name of the file:\t")
background = Back(text,file)
background.start()
print "File being written in background."
print "Foreground task: add" +  str(10+30)
background.join()	#waits till the thread is complete
print  "Waited for the thread to complete."