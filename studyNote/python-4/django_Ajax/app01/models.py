from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Class(models.Model):
    """班级"""
    title=models.CharField(max_length=32)
    m=models.ManyToManyField("Teacher",related_name="foo")

class Teacher(models.Model):
    """老师"""
    name=models.CharField(max_length=32)

class Student(models.Model):
    """学生"""
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    gender=models.BooleanField()
    cs=models.ForeignKey("Class",on_delete=models.CASCADE)
