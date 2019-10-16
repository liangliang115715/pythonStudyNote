#_author: 
#date:

# 字典操作：增
dic1={"name":"ll"}
dic1["hobby"]="basketball"#已存在的会被修改
print(dic1)
b=dic1.setdefault("heigh",176)#键存在，返回函数值；键不存在，增加进字典
                              # setdefaul函数返回值为后一个元素的值
print(b)
print(dic1)
# 字典 操作方法：查&改&删

# print(dic1.keys()) # 取键 可用list（）转换输出的形式
# print(dic1.values())#取值  可用list（）转换输出的形式
# print(dic1.items())# 取键值对  可用list（）转换输出的形式

dic2={"name":"liangliang","shoes":"black"}
# dic1.update(dic2) # update 更新字典 原有的会被覆盖，没有的会添加
# print(dic1)
# print(dic2)

# del dic2["shoes"]  # del 删除shoes键值对
# print(dic2)

# dic2.clear()  # clear 清空字典 剩下一个空的字典
# print(dic2)

# ret=dic2.pop("shoes") # pop 按键删除，有返回值：键值对的“值”
# print(ret)
# print(dic2)

# a=dic2.popitem() # popitem 随机删除一对键值，并以元组的方式返回值
# print(dic2)

# 其他操作方法

# dic3=dict.fromkeys(["host1","host2","host3"],["test","exam","wawa"])
# print(dic3)   #   fromkeys 只能统一赋一样的值，相当于初始化；改动也只会改成统一的值
# dic3["host2"][1]= "huhu"
# print(dic3) # {'host1': ['test', 'huhu', 'wawa'], 'host2': ['test', 'huhu', 'wawa'], 'host3': ['test', 'huhu', 'wawa']}

# print(sorted(dic2.values())) # sorted（） 按（）排序，不加（）默认按键排序

# 遍历输出字典的两种方式，推荐第一种 ，第二种items有转换，效率低
for i in dic2:
	print(i,dic2[i])
#
# for j,k in dic2.items():
# 	print(j,k)


