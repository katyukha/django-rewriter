# -*- coding: utf-8 -*-
from django import forms
from django.forms import widgets

class ProfileForm (forms.Form):
	f_name = forms.CharField(label = "Имя")
	l_name = forms.CharField(label = "Фамилия")
	phone  = forms.CharField(label = "Телефон", max_length = 20)
