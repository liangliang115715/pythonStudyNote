# Generated by Django 2.1.7 on 2019-02-25 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='课程名称')),
                ('summy', models.CharField(max_length=200, verbose_name='课程简介')),
                ('img', models.ImageField(upload_to='', verbose_name='课程LOGO')),
            ],
        ),
        migrations.CreateModel(
            name='Companny',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ComPhoto', models.ImageField(upload_to='', verbose_name='公司LOGO')),
                ('ComAddr', models.CharField(max_length=48, verbose_name='链接地址')),
            ],
        ),
        migrations.CreateModel(
            name='HeadPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.BooleanField()),
                ('name', models.CharField(max_length=32)),
                ('target', models.CharField(max_length=48)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('summy', models.CharField(max_length=200, verbose_name='简介')),
                ('detail', models.CharField(max_length=1000, verbose_name='更多信息')),
            ],
        ),
        migrations.DeleteModel(
            name='stu',
        ),
    ]
