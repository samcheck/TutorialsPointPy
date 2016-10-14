#!/usr/bin/python3
# multiThreadingEx.py - demo multithreading w/ custom class and delay/counter

# To implement a new thread using the threading module, you have to do the following:
#	- Define a new subclass of the Thread class.
#	- Override the __init__(self [,args]) method to add additional arguments. 
#	- Then, override the run(self [,args]) method to implement what 
#		the thread should do when started.  
# Once you have created the new Thread subclass, you can create an instance 
# of it and then start a new thread by invoking the start(), 
# which in turn calls run() method.


import threading, time

exitFlag = 0

class myThread(threading.Thread):
	def __init__(self, threadID, name, counter, delay):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		self.delay = delay
	def run(self):
		print("Starting " + self.name)
		print_time(self.name, self.counter, self.delay)
		print("Exiting " + self.name)
		
def print_time(threadName, counter, delay):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print("%s: %s" % (threadName, time.ctime(time.time())))
		counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 5, 2)
thread2 = myThread(2, "Thread-2", 10, 1)
thread3 = myThread(3, "The Third", 7, 3)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print("Exiting Main Thread")
