#_author: Administrator
#date:  
"呦，又在写bug呐！！！"
import time,os
from multiprocessing import Process
def func1(*args):
	time.sleep(0.1)
	print(args[0])
	print("%s号子进程的父进程>>:"%args[1],os.getppid())  #查看当前进程的父进程
	

if __name__ == '__main__':
	# P = Process(target=func1,args=((1,2,4))) # 创建进程对象
	# P.start()
	# print(">>>>>>>>>>>>>")
	# print("当前进程>>:",os.getpid())# 查看当前进程  11252
	# # 执行结果：>>>>>>>>>>>>>
	# 			# -----------
	# #说明新开进程与本页面进程同时执行，不存在绝对的先后顺序
	
	p_lst = []
	print ("当前进程>>:", os.getpid ())
	for i in range(10):
		p = Process(target=func1,args=("*********",i))
		p.start()
		p_lst.append(p)
	[p.join() for p in p_lst]
	print("任务结束")

	