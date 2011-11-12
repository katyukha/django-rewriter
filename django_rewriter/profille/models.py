# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    url = models.URLField("Домашня сторінка: ", blank=True)
    UserInfo = models.TextField("Інформація про себе: ",blank=True)

@receiver(post_save, sender=User)
def profileuser_save (sender,instance, created, **kwargs):
	if created:
		profile = UserProfile(user = instance)
		profile.save()
		
