# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    url = models.URLField("Website", blank=True)
    UserInfo = models.TextField(blank=True)

@receiver(post_save, sender=User)
def ProfileUser (sender,instance, created, **kwargs):
	if created:
		UserProfile(user = instance).save()
#post_save.connect(profileUser,sender=UserProfile)
