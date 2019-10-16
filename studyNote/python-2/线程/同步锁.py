#_author: 
#date:
"""
同步锁解决的是开多线程时cpu频繁切换过程中造成的数据混乱
开启同步锁时之前的内容照常切换执行但只能等锁住的内容执行完毕时
下一线程才能重新拿到GIL锁
"""
import threading,time

def DevNum():
	global num
	
	# num-=1
	
	# temp=num
	# num=temp-1
	# print("*")
	# 调用同步锁
	lock.acquire()
	temp=num
	time.sleep(0.00001)
	num=temp-1
	#关闭同步锁
	lock.release()

num=100
threads=[]
# 添加线程同步锁
lock=threading.RLock()

for i in range(100):
	t=threading.Thread(target=DevNum)
	t.start()
	threads.append(t)
for t in threads:
	t.join()

print("final time:",num)
# print(threads)