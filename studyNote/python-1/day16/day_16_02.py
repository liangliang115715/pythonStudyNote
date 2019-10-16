#_author: 
#date:

import time
def logger(flag=""):# 再嵌套一层可以给装饰器加参数
	def show_time(f):
		def inner(*args):
			start=time.time()
			f(*args)
			end=time.time()
			print("spend %s"%(end-start))
			if flag=="true":
				print("日志记录")
		return inner
	return show_time

@logger("true")# 相当于add=show_time(add)
def add(*args):
	ans=0
	for i in args:
		ans+=i
	print(ans)
	time.sleep(2)

add(2,8,7,5,6,2,4)
