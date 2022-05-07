from tkinter import W
from django import forms
from accounts.admin import UserCreationForm
from accounts.models import  User
from django.db import models



class Course(models.TextChoices):
    FYBCS = 'FY19', ('FYB.sc Computer science')
    SYBCS = 'SY19', ('SYB.sc Computer science')
    TYBCS = 'TY19', ('TYB.sc Computer science')

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=254,required=True,widget=forms.TextInput())
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    course_name = forms.ChoiceField(choices=Course.choices, widget=forms.Select)
    class Meta:
        model = User
        fields = ('username', 'email','course_name', 'password1', 'password2')