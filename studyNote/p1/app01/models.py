from django.db import models

# Create your models here.
# 单表
class HeadPhoto(models.Model):
	weight=models.BooleanField("权重")
	name=models.CharField("标题",max_length=32)
	target=models.CharField("链接地址",max_length=48)
	img=models.CharField("图骗地址",max_length=48)
	class Meta:
		verbose_name_plural = "轮播图"
	def __str__(self):
		return self.name
class Companny(models.Model):
	# ComPhoto=models.ImageField("公司LOGO",upload_to='')
	name=models.CharField("公司名称",max_length=32)
	ComPhoto=models.CharField("公司LOGO",max_length=48)
	ComAddr=models.CharField("链接地址",max_length=48)
	class Meta:
		verbose_name_plural = "企业合作"
	def __str__(self):
		return self.name
class News(models.Model):
	# display=models.BooleanField()
	# weight=models.IntegerField("")
	title=models.CharField("标题",max_length=32)
	summy=models.CharField("简介",max_length=200)
	detail=models.CharField("更多信息",max_length=1000)
	class Meta:
		verbose_name_plural = "最新公告"
	def __str__(self):
		return self.title
class Classes(models.Model):
	name=models.CharField("课程名称",max_length=16)
	summy=models.CharField("课程简介",max_length=200)
	img=models.CharField("课程LOGO",max_length=48)
	class Meta:
		verbose_name_plural = "课程"
	def __str__(self):
		return self.name

#一对一表
class StudentInfo(models.Model):
	name=models.CharField("姓名",max_length=32)
	age=models.IntegerField("年龄")
	worksFor=models.CharField("所属公司",max_length=32)
	img=models.CharField("个人照",max_length=48)
	summy=models.CharField("简介",max_length=200)
	salary=models.FloatField("薪资/月")
	more=models.OneToOneField("StudentMore",on_delete=models.CASCADE,verbose_name='更多信息')
	class Meta:
		verbose_name_plural = "学生信息"
	def __str__(self):
		return self.name

class StudentMore(models.Model):
	moreInfo=models.CharField("更多想说的",max_length=1000)
	class Meta:
		verbose_name_plural = "学生更多信息"
	def __str__(self):
		return "想...."
#多对多表
class direction(models.Model):
	name=models.CharField("方向",max_length=32)
	subject=models.ManyToManyField("subject")
	class Meta:
		verbose_name_plural = "筛选方向"
	def __str__(self):
		return self.name
class subject(models.Model):
	name=models.CharField("学科",max_length=32)
	class Meta:
		verbose_name_plural = "筛选学科"
	def __str__(self):
		return self.name
#一对多表
class grade(models.Model):
	name=models.CharField("等级",max_length=32)
	class Meta:
		verbose_name_plural = "筛选等级"
	def __str__(self):
		return self.name

class videos(models.Model):

	subject=models.ForeignKey("subject",on_delete=models.CASCADE)
	grade=models.ForeignKey("grade",on_delete=models.CASCADE)

	title=models.CharField("标题",max_length=32)
	href=models.CharField("链接地址",max_length=32)
	img=models.CharField("图片链接",max_length=32)
	class Meta:
		verbose_name_plural = "筛选视频"
	def __str__(self):
		return self.title
class imgs(models.Model):

	img = models.FileField("图片",upload_to="static/images")
	src=models.CharField("图片链接",max_length=48)
	title = models.CharField("标题",max_length=16)
	sumary= models.CharField("简介",max_length=128)

	class Meta:
		verbose_name_plural = "图片集"

	def __str__(self):
		return self.title
	