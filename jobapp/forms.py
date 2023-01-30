from django import forms

# registration
from django.contrib.auth.models import User

from .models import *


class regform(forms.Form):
    company=forms.CharField(max_length=20)
    email=forms.EmailField()
    address=forms.CharField(max_length=300)
    phone=forms.IntegerField()
    password=forms.CharField(max_length=10)
    cpassword = forms.CharField(max_length=10)


class logform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=10)



# upload vacancies
class uploadform(forms.Form):
    company=forms.CharField(max_length=20)
    email = forms.EmailField()
    job = forms.CharField(max_length=20)
    jobtype = forms.CharField(max_length=20)
    worktype = forms.CharField(max_length=20)
    experience = forms.CharField(max_length=20)
    qualification = forms.CharField(max_length=20)

# using user model
class reg(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password","first_name","last_name"]

class log(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=10)

# using class based and modelform
class userform(forms.ModelForm):
    class Meta:
        model=usermodel
        fields='__all__'

class applyform(forms.Form):
    company=forms.CharField(max_length=20)
    job=forms.CharField(max_length=20)
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    resume=forms.FileField()