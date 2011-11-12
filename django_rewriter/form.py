# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.forms import widgets
from django_rewriter.profille.models import UserProfile

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile

class ProfileForm2 (forms.Form):
	f_name = forms.CharField("Ім'я: ")
	l_name = forms.CharField("Фамілія: ")
	url = forms.URLField("Домашня сторінка: ")
	UserInfo = forms.CharField("Інформація про себе: ", widget = widgets.Textarea)
