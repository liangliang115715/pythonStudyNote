# Generated by Django 2.1.7 on 2019-02-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20190225_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companny',
            name='ComPhoto',
            field=models.ImageField(upload_to='', verbose_name='公司LOGO'),
        ),
    ]