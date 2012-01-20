# -*- coding: utf-8 -*-
from django import forms
from django.forms import widgets

class ProfileForm (forms.Form):
	f_name = forms.CharField(label = "Имя", required = True)
	l_name = forms.CharField(label = "Фамилия", required = True)
	phone  = forms.CharField(label = "Телефон", required = True, max_length = 20)
	email = forms.EmailField(widget=forms.TextInput(attrs=dict(maxlength=75)))
