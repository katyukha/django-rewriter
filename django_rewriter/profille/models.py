# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user      = models.OneToOneField(User, unique=True)
    url       = models.URLField("Домашня сторінка: ", blank=True)
    user_info = models.TextField("Інформація про себе: ",blank=True)
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

