#_author: 
#date:
# # 生成器例子
# import time
# def consume(name):
# 	print("%s准备吃包子了"%name)
# 	while True:
# 		baozi=yield
# 		print("包子[%s]被[%s]吃了"%(baozi,name))
#
# def produce(name):
# 	c1=consume("a")
# 	c2=consume("b")
# 	next(c1)
# 	next(c2)
# 	print("%s开始做包子了"%name)
# 	for i in range(10):
# 		time.sleep(1)
# 		print("做了两个包子")
# 		c1.send(i)# 执行c1即consume("a"),并把i发送给yield
# 		c2.send(i)
# produce("alxe")

# # 生成五位验证码：
# import random
# def suijishu():
# 	code=""
# 	for i in range(5):
# 		add=random.choice([random.randint(0,9),chr(random.randint(65,90))])
# 		code+=str(add)
# 	print(code)
# suijishu()

