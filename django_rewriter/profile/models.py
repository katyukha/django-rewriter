# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.db.models.signals import class_prepared

class UserProfile(models.Model):
    user      = models.OneToOneField(User, unique=True)
    phone     = models.CharField("Телефон", max_length = 20)
    is_seo    = models.BooleanField(default = False)
    sync      = models.BooleanField(default = True)
    
    def save(self, *args, **kwargs):
        self.sync = True
        return super(UserProfile, self).save(*args, **kwargs)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])



# catch signals:
from registration import signals

def on_register(sender, user, **kwargs):
    user.active = False
    user.save()

signals.user_registered.connect(on_register)


def on_user_save (sender, instance, **kwargs):
        if instance.pk:
            p = instance.profile
            p.sync = True
            p.save()

pre_save.connect (on_user_save,            sender = User)
