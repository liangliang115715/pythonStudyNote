#_author: 
#date:


dict_list={
	         "A_sheng":{
		         "a_shi":("a1_xian","a2_xian","a3_xian"),
	         },
	         "B_sheng":{
		         "b_shi":("b1_xian","b2_xian","b3_xian")
	         },
	         "C_sheng":{
		         "c_shi":("c1_xian","c2_xian","c3_xian"),
	         },
}
while True:
	for key in dict_list:
		print(key)
	sheng=input("输入要详细查看的省（退出：quit）：")
	if sheng in dict_list:
		while True:
			for key2 in dict_list[sheng]:
				print(key2)
			shi = input("输入要详细查看的市（返回上一层：back）：")
			if shi in dict_list[sheng]:
				while True:
					for key3 in dict_list[sheng][shi]:
						print(key3)
					last=input("这是最后一层了（返回上一层：back）")
					if last=="back":
						break
			elif shi == "back":
				break
			else:
				print("非法字符！！！")
				
	elif sheng == "quit":
		break
	else:
		print("非法字符！！！")
  
		
