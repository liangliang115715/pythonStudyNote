#_author: 
#date:

import threading,time
class myThread(threading.Thread):
	def doA(self):
		lock.acquire()
		print(self.name,"getlockA",time.ctime())
		time.sleep(0.3)
		lock.acquire()
		print(self.name,"getlockB",time.ctime())
		lock.release()
		lock.release()
		time.sleep(0.01)
	def doB(self):
		lock.acquire()
		print(self.name,"getlockB",time.ctime())
		time.sleep(0.2)
		lock.acquire()
		print(self.name,"getlockA",time.ctime())
		lock.release()
		lock.release()
	def run(self):
		self.doA()
		self.doB()
# lockA=threading.Lock()
# lockB=threading.Lock()
if __name__ == '__main__':
	# Rlock 递归锁 可设置多把锁而不造成死锁现象
	lock=threading.RLock()
	#   lock 易造成死锁现象
	# lockA = threading.Lock()
	# lockB = threading.Lock()
	
	threads=[]
	for i in range(5):
		threads.append(myThread())
	for t in threads:
		t.start()
	for t in threads:
		t.join()