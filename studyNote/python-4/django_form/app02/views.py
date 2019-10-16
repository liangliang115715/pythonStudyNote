from django.shortcuts import render,redirect,HttpResponse
from django import forms
from django.forms import fields


class textForm(forms.Form):
    username=fields.CharField(
        required=True,
        max_length=12,
        error_messages={
            "required":"皆空",
            "max_length":"超长",
        },
    )
    age=fields.IntegerField(
        required=True,
        error_messages={
            "required": "皆空",
            "invaild":"贫僧，贱尼"
        }
    )
    email=fields.EmailField(
        required=True,
        error_messages={
            "required": "皆空",
            "invaild":"贫僧，贱尼"
        }
    )

def text(request):

    obj=textForm()

    return render(request,"text.html",{"obj":obj})


