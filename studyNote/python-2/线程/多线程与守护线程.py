#_author: 
#date:

import threading,time

def foo(n,y):
	sum=0
	for i in range(n):
		sum+=i
	time.sleep(y)
	print(sum)

t1=threading.Thread(target=foo,args=(10,2,))
t2=threading.Thread(target=foo,args=(100,3,))

threads=[t1,t2]
if __name__=="__main__":
	for t in threads:
		""" 主程序等待所有非Daemon线程结束后才退出，
		    且退出时会自动结束（很粗鲁的结束）所有Daemon线程
		    守护的是主线程"""
		t.setDaemon(True)
		t.start()
	#在子线程完成运行之前，该子线程的父线程（一般就是主线程）将一直存在，
	# 也就是被阻塞
	t2.join()
	print("all over")



