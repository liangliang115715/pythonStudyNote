#_author: 
#date:


product_list=[
	("mac",9000),
	("kindle",800),
	("tesla",900000),
	("python book",105),
	("bike",2000),
]
shopping_car=[]
saving=int(input("please input your saving:"))

while True :
	# 遍历输出购物单 enumerate(_,_) 枚举 可用作编号，第二个参数为起始编号
	for i,v in enumerate(product_list,1):
		print(i,"...",v)
	# 引导用户输入需要的商品单号
	choice=input("please input the number you want[quit:q]")
	# 判断输入的合法性 1.合法 进购买程序  2.退出字符（q） 打印已购买商品 然后退出 3.非法字符 通过循环重新输入
	if choice.isdigit():
		choice=int(choice)
		if choice>0 and choice<=len(product_list):
			p_item=product_list[choice-1]
			if p_item[1]<saving:
				saving=saving-p_item[1]
				shopping_car.append(p_item)
			else:
				print("no enough money,and %s you have"%saving)
			print(p_item, "have been extend your shopping car")
		else:
			print("invalid input ")
	elif choice=="q":
		print("----------you have buy these----------")
		for t in shopping_car:
			print(t)
		print("the money you left %s"%saving)
		break
	else:
		print("invalid input")