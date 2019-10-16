from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django import forms
from django.forms import fields

class F1Form(forms.Form):
    user=fields.CharField(
        max_length=18,
        min_length=6,
        required=True,
        error_messages={
            "required":"皆空?",
            "max_length":"超长？",
            "min_length":"略短？",
        }
    )
    pwd=fields.CharField(
        min_length=10,
        required=True,
        error_messages={
            "required": "皆空?",
            "min_length": "略短？",
        }
    )
    age=fields.IntegerField(
        required=True,
        error_messages={
            "required": "皆空?",
            "invalid": "阿拉伯数字啊，老铁",
        }
    )
    email=fields.EmailField(
        required=True,
        error_messages={
            "required": "皆空?",
            "invalid": "无法无天？",
        }
    )



def f1(request):
    if request.method =="GET":
        obj=F1Form()
        return  render(request, "f1.html",{"obj":obj})
    elif request.method == "POST":
        # user=request.POST.get("user")
        # psw=request.POST.get("psw")
        # email=request.POST.get("email")
        obj=F1Form(request.POST)
        #是否验证成功
        if obj.is_valid():
            #用户提交的数据
            print("验证成功",obj.cleaned_data)
            return redirect("https://www.baidu.com")
        else:
            print("验证失败",obj.errors)
            return render(request,"f1.html",{"obj":obj})

    return HttpResponse("ok")