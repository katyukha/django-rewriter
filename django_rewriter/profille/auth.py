# -*- coding: utf-8 -*-
# django imports
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _

# rewriters imports
from registration.backends.simple import SimpleBackend
from registration import signals
from registration.forms import RegistrationFormUniqueEmail
from registration.forms import attrs_dict

class InactiveSimpleBackend(SimpleBackend):
     """
         This backend simply creates inactive user.
     """
     def register(self, request, **kwargs):
        username, email, password = kwargs['username'], kwargs['email'], kwargs['password1']
        new_user = User.objects.create_user(username, email, password)
        new_user.is_active = False
        new_user.save()

        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

class InactiveProfileRegisterBackend(SimpleBackend):
    """
        Backend to register inactive user with filled extra information.
    """
    def register(self, request, **kwargs):
        k = kwargs
        new_user = User.objects.create_user(k['username'], k['email'], k['password1'])

        new_user.is_active    = False
        new_user.first_name   = k['first_name']
        new_user.last_name    = k['last_name']

        new_user.save()

        profile       = new_user.profile
        profile.phone = k['phone']
        profile.save()

        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

class RegistrationFormExtraInfo(RegistrationFormUniqueEmail):
    """ Form to make users fill more information during registration.
    """
    first_name = forms.CharField(
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label="Имя",
                                )
    last_name  = forms.CharField(
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label="Фамилия",
                                )
    phone      = forms.CharField(
                                max_length=20,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label="Телефон",
                                )