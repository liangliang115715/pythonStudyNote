#_author: 
#date:


class section:
	def __init__(self,name,sex,age,star_power):
		self.name=name
		self.sex=sex
		self.age=age
		self.power=float(star_power)
		global power
	def caocong(self):
		self.power-=200
		print("%s 草丛战斗 战力剩余%s"%(self.name,self.power))
	def selfpractice(self):
		self.power+=100
		print("%s 自我修炼 战力剩余%s"%(self.name,self.power))
	def connet_game(self):
		self.power+=500
		print("%s 多人游戏 战力剩余%s" %(self.name,self.power))
obj1=section("苍井井","女","18","1000")
obj2=section("东尼木木","男","20","1800")
obj3=section("波多多","女","19","2500")

obj1.caocong()
