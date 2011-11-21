# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user      = models.OneToOneField(User, unique=True)
    url       = models.URLField("Домашняя страница: ", blank=True)
    user_info = models.TextField("Информация о себе: ",blank=True)
    is_seo    = models.BooleanField(default = False)
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

