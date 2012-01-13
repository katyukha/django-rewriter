# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

class UserProfile(models.Model):
    user      = models.OneToOneField(User, unique=True)
    phone     = models.CharField("Телефон", max_length = 20)
    is_seo    = models.BooleanField(default = False)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])







# MONKEYS.      DARK MAGIC IS HERE. Sync field added to User model
# user sync field
sync_field   =   models.BooleanField (default = True)
sync_field.contribute_to_class (User, 'sync')


def on_user_save (sender, instance, **kwargs):
        instance.sync = True

pre_save.connect (on_user_save,            sender = User)
