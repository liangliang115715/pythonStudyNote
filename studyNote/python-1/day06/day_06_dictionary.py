#_author: 
#date:


# b=0
# print(id(b))
# print(id(0))
# 整形数字有自己的地址 ，而定义的变量本身没有地址
# 变量只是借用了整形数字的地址，它本身成为了这个整形数字的牌面

#dic 链表存储？通过对应关系和首项找到冒号后面的项 dic相当于映射关系
dic={"name":"冫冫","age":20,"hobby":"basketball","profassion":"student"}
# print(dic["age"])
# print(id(dic["age"]))

dic2=dict((("name","ll"),("age",12)))
print(dic2)