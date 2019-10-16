#_author: 
#date:

# 加密模块
# import hashlib

# m=hashlib.md5()
# print(m)
# m.update("hello world".encode("utf8"))
# # 默认unicode类型需转换为当前编码类型
# print(m.hexdigest())# hexdigest：十六进制输出
#
# m.update("ll".encode("utf8"))
# print(m.hexdigest())#a3d405020028c9192ca5dee93f388c32
#
# m2=hashlib.md5()
# m2.update("hello worldll".encode("utf8"))
# print(m2.hexdigest())
# #a3d405020028c9192ca5dee93f388c32 说明先后两次update其实是字符串拼接到了一起

# 日志模块
import logging
# # 设置日志格式：
# logging.basicConfig(level=logging.DEBUG,#调整输出等级  （debug-info-warning-error-critical 逐级递增）
#                     format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
#                     datefmt="%a,%d %b %Y %H:%M:%S",#asctime 设置时间格式
#                     filename="test.log",# 生成日志所在位置及文件名字
#                     filemode="a")        # 设置文件操作模式
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message,beach")
# logging.error("error message,fool")
# logging.critical("critical message,son")

#创建一个logger对象
logger=logging.getLogger()
#创建一个handle用于写入日志文件
fh=logging.FileHandler("text1.log")
#再次创建一个handle，用于输出带控制台
ch=logging.StreamHandler()
# 设置输出格式
formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
# fh,ch分别调用设定的输出格式 （set:设定）
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 选用何种方法即选用输出到哪里  fh：日志文件 ch：控制台
logger.addHandler(fh)
logger.addHandler(ch)

# 选用输出等级
logger.setLevel(logging.DEBUG)

#调用logger方法选择写入的等级和内容
logger.debug("hello debug")
logger.info("hello info")
logger.warning("hello warning")
logger.error("hello error")
logger.critical("hello critical")

