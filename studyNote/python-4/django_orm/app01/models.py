from django.db import models

# Create your models here.


class Book(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    pub_data=models.DateField()
    author=models.CharField(max_length=32,null=False)
    publish = models.ForeignKey('Publish', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name


class Publish(models.Model):
    # id=models.ForeignKey(Book,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    date=models.DateField()


