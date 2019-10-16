
from django import forms as dforms
from django.forms import fields

class UserForms(dforms.Form):
    username=fields.CharField(max_length=20)
    email=fields.EmailField()
