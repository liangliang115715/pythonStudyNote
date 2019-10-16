#_author: 
#date:
"""
class BaseRequest:
	def sever_forever(self):
		pass

class RequestHandler(BaseRequest):
	
	def sever_forever(self):
		# 此处self=obj
		print("RequestHandler.sever_forever")
		self.process_request()#从原点开始找process_request方法
	
	
	def process_request(self):
		print("RequestHandler.proces_request")

class Minx:

	def process_request(self):
		print("Minx.process_request")
	

class son(Minx,RequestHandler):
	pass
obj=son()
obj.sever_forever()
"""

class foo:
	def __init__(self):
		pass
	def __getitem__(self, item):
		print(item)
		print(type(item))



obj=foo()
ret=obj[1:4:2]
print(ret)

























