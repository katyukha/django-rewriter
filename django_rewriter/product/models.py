# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('draft',    u'Черновой'),
    ('progress', u'В работе'),
    ('deferred', u'Отложенный'),
    ('done',     u'Выполнено'),
    ('accepted',     u'Принятый'),
    ('rejected', u'Отклонено')
)

    
class Product(models.Model):
    user = models.ForeignKey(User, blank = True, null = True)
    name = models.CharField("Название", max_length = 50,
                        help_text = "* Это поле обязательно для заполнения.")
    code = models.CharField("Код",max_length=10,blank=True)
    brief_desc = models.CharField("Краткое описание",max_length = 250,
                        blank = True,)
    full_desc = models.TextField("Полное описание",blank = True)
    meta_title = models.CharField("Мета-заголовок",max_length = 50,
                        blank=True)
    meta_keywords = models.CharField("Ключевые слова",max_length = 200,
                        blank=True)
    meta_desc = models.CharField("Мета-описание",max_length=250,
                        blank=True)
    rating = models.IntegerField("Оценка",blank=True, null = True)
    status = models.CharField("Состояние", max_length=15, choices=STATUS_CHOICES,
                        blank=True, default="draft")
    '''image = models.ImageField("Изображение", upload_to = "/static/photos/")

    def save(self):
        for field in self._meta.fields:
            if field.name == 'image':
                field.upload_to = 'static/photos/%d' %self.id
        super(Product, self).save()'''

    def __unicode__(self):
        return "%s [%s]" % (self.name, self.code)
