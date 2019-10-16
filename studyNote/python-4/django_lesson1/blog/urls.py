from django.contrib import admin
from django.urls import path,re_path
from blog import views

urlpatterns = [
    #无命名匹配
    re_path('index1/(\d{4})$', views.index1),
    #有命名匹配  命名与传给views的参数名字必须保持一致
    re_path('index2/(?P<year>\d{4})/(?P<month>\d{2})', views.index2),
    re_path('register', views.register,name="reg"),
]