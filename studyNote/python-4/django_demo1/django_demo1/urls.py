"""django_demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app01.views import classes,teachers,students,ajax

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('classes.html$', classes.get_classes),
    re_path('add_classes$', classes.add_classes),
    re_path('del_classes$', classes.del_classes),
    re_path('edit_classes$', classes.edit_classes),

    re_path('students.html$', students.get_students),
    re_path('add_students$', students.add_students),
    re_path('del_students$', students.del_students),
    re_path('edit_students$', students.edit_students),

    re_path('set_teachers$', teachers.set_teachers),

    re_path('ajax1.html$', ajax.ajax1),

]





