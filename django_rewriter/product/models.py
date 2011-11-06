# -*- coding: utf-8 -*-
from django.db import models

STATUS_CHOISES = (
    ('draft',u'Чорновий'),
    ('during',u'В роботі'),
    ('deferred',u'Вiдкладений'),
    ('done',u'Виконано'),
    ('recd',u'Прийнятий'),
    ('rejected',u'Вiдхилений')
)
class Product(models.Model):
    code = models.CharField(max_length=10)
    brief_desc = models.CharField(max_length=250)
    full_desc = models.TextField()
    meta_title = models.CharField(max_length=50)
    meta_keywords = models.CharField(max_length=200)
    meta_desc = models.CharField(max_length=250)
    rating = models.IntegerField()
    status = models.CharField(choises=STATUS_CHOISES)

