#_author: 
#date:


import re

# “.”:通配符 换行符不可匹配
s="hello world"
# ret=re.findall("w..l","%s"%(s))
# print(ret)

# “^”：只在开头开始匹配
# ret=re.findall("^w..l","%s"%(s))
# print(ret)

#“$”：只在末尾匹配
# ret=re.findall("o..d$","%s"%(s))
# print(ret)

# “*”:重复匹配 可重复*前字符多次([0,+oo]次)
# ret=re.findall("w.*d","%s"%(s))
# print(ret)

#"+":重复匹配 可重复+前字符多次([1,+oo]次)
# ret=re.findall("w+d","%s"%(s))
# print(ret)

# ? 只能取[0,1]次
# ret=re.findall("w?d","%s"%(s))
# print(ret)

# {}任意匹配次数,有范围的优先取最大的次数--贪婪匹配，{1，}右边不加代表正无穷
# ret=re.findall("a{5}b","vaaaaab")
# print(ret)
# ret=re.findall("a{1,3}b","aaaaab")
# print(ret)

#重复类的推荐用 ？，+，*

# [] :或关系 内部可取消字符的特殊功能。
# ret=re.findall("a[c,d]x","acx")
# print(ret)#['acx']
# ret=re.findall("a[c,d]x","adx")
# print(ret)#['adx']
# ret=re.findall("a[c,d]x","acdx")
# print(ret)#[]

# ret=re.findall("a[c,*]x","acdx")
# print(ret)#[]


#[] 中用 - 表范围
# ret=re.findall("[a-z]","acxasdsadasd")
# print(ret)#['a', 'c', 'x', 'a', 's', 'd', 's', 'a', 'd', 'a', 's', 'd']

# ret=re.findall("[1-9a-zA-Z]","12PUpu")#[1-9a-zA-Z]与[1-9,a-z,A-Z]效果相同
# print(ret) #['1', '2', 'P', 'U', 'p', 'u']

# ^ 放在[]内表取反（可取除此元素外所有字符）
# ret=re.findall("[^t]","act54dx")
# print(ret)#['a', 'c', '5', '4', 'd', 'x']

# [^5,4]  非5或者非4,除去[]内所有的字符
# ret=re.findall("[^5,,4]","act54dx,,")
# print(ret)#['a', 'c', 't', 'd', 'x']

# \其后跟元字符去除特殊功能，后跟一部分普通字符实现特殊功能
#\d	数字:[0-9]
# \D	非数字:[^\d]
# \s	匹配任何空白字符:[<空格>\t\r\n\f\v]
# \S	非空白字符:[^\s]
# \w	匹配包括下划线在内的任何字字符:[A-Za-z0-9_]
# \W	匹配非字母字符，即匹配特殊字符
# \A	仅匹配字符串开头,同^
# \Z	仅匹配字符串结尾，同$
# \b	匹配\w和\W之间，即匹配单词边界匹配一个单词边界，也就是指单词和特殊字符间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
# \B	[^\b]


#################################################

# re.search()方法匹配出第一个满足条件的结果
# ret=re.search("sb","sbghjsb")
# print(ret)#<_sre.SRE_Match object; span=(0, 2), match='sb'>
# print(ret.group())#sb

# ret=re.search("a\+","a+gj").group()
# print(ret) # a+


# () 分组 匹配（）内这个组的内容
# print(re.search("(as)+","dfsfasas").group())
# print(re.search("(as)|3","3dfsfasas").group()) # | 是或的意思


# match方法 只在字符串开始匹配，只返回匹配到的第一个对象，用法和search相同

# split方法
# ret=re.split("k","dsaksfa")
# print(ret)#['dsa', 'sfa']

# ret=re.split("[s,f]","dsaksfa")
# print(ret)#['d', 'ak', '', 'a'] 先以s分 再将分之后的结果以f分，空字符是因为f前为空字符

# sub 替换
# ret=re.sub("s.k","nb","dsaksfa")
# print(ret)#dnbsfa
#命令：re.sub(pattern, repl, string, count=0, flags=0)
#              re.sub 用于替换字符串的匹配项。如果没有匹配到规则，则原字符串不变。
#
#             第一个参数：规则
#             第二个参数：替换后的字符串
#             第三个参数：字符串
#             第四个参数：替换个数。默认为0，表示每个匹配项都替换

# compile 方法 可将同一匹配规则调用不同方法
# re.findall("\.com","fasdf,comsadfa")
# obj=re.compile("\.com")
# ret=obj.findall("fasdf.comsadfa")
# print(ret)#['.com']

