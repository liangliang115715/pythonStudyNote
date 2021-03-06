"""FenYe URL Configuration

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
from app01 import views
from app02 import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('index.html$', views.index),
    re_path('index1.html$', views.index1),
    re_path('index2.html$', views.index2),
    re_path('f1.htmls$', v2.f1),
]
