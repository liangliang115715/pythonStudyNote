#_author: 
#date:


f1=open("jingdong","r",encoding="utf8")
f2=open("weixin","r",encoding="utf8")
dict_f1=eval(f1.read().strip())
dict_f2=eval(f2.read().strip())
log="false"


def login(ttt):
	def login_in(f):
		def inner():
			global log
			if log=="false":
				pingtai=input("which is your choice:1.jingdong 2.weixin")
				if pingtai=="1" or pingtai=="2":
					username=input("input username:")
					password=input("input password:")
					if pingtai == "1":
						if username in dict_f1 and password==dict_f1[username]:
							print("login succed")
							f()
							log="true"
						else:print("the error")
					if pingtai == "2":
						if username in dict_f2 and password==dict_f2[username]:
							print("login succed")
							f()
							log = "true"
						else:print("the error")
				else:
					print("invaliad input")
			else: return f
		return inner
	return login_in
# def func():
# 	fun=login("true")
# 	dict_f1=eval(f1.read().strip())
# 	dict_f2=eval(f2.read().strip())
# 	fun(dict_f1,dict_f2)
@login("jing")# 先执行login（“jing”），函数返回为login_in即装饰器函数
def home():
	print("this is the home page")
@login("jing")
def pc():
	print("this is the pc page")
@login("jing")
def book():
	print("this is the pc page")

def main():
		choice=input("""welcome to the func,please choose the page you want to reach!!!
		            >>>1.home
		            >>>2.pc
		            >>>3.book
		            >>>4.quit  """)
		if choice=="1":home()
		elif choice=="2":pc()
		elif choice=="3":book()
		elif choice=="4":exit()
		else:print("the error input")

main()
