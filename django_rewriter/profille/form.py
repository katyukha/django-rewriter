# -*- coding: utf-8 -*-
from django import forms
from django.forms import widgets

class ProfileForm (forms.Form):
	f_name = forms.CharField(label = "Имя")
	l_name = forms.CharField(label = "Фамилия")
	url = forms.URLField(label = "Домашняя станица")
	user_info = forms.CharField(label = "Информация о себе", widget = widgets.Textarea)
