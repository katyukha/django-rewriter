# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = (
    ('draft',      u'Черновой'),
    ('progress',   u'В работе'),
    #('deferred',   u'Отложенный'),
    #('wait_check', u'Ожидает проверки'),
    ('check',      u'Проверяеться'),
    ('accepted',   u'Принятый'),
    ('rejected',   u'Отклонено')
)

    
class Product(models.Model):
    user = models.ForeignKey(User, blank = True, null = True)

    # head fields
    name = models.CharField("Название", max_length = 128)

    code = models.CharField("Код",max_length=64,blank=True)
    
    # description fields
    brief_desc = models.TextField("Краткое описание",max_length = 350,
                        blank = True,)
    full_desc = models.TextField("Полное описание",blank = True)
    
    # meta fields
    meta_title = models.CharField("Мета-заголовок",max_length = 128,
                        blank=True)
    meta_keywords = models.TextField("Ключевые слова",max_length = 500,
                        blank=True)
    meta_desc = models.TextField("Мета-описание",max_length=500,
                        blank=True)

    # state fields
    rating = models.IntegerField("Оценка",blank=True, null = True)
    status = models.CharField("Состояние", max_length=15,
                        choices=STATUS_CHOICES, blank=True,
                        default="draft")
                        
    # requirements fields
    required_full_desc    = models.BooleanField("Требуется полное описание",
                                                default = False)
    required_brief_desc   = models.BooleanField("Требуется краткое описание",
                                                default = True)
    required_meta_info    = models.BooleanField("Требуестя мета-информация",
                                                default = False)
    required_images_count = models.IntegerField("Требуемое количество изображений",
                                                default = 0)
    
    # sync fields
    sync                  = models.BooleanField("Need to sync?", default = True)
                            # True means that record was moddified from last sync.

    def __unicode__(self):
        return "%s [%s]" % (self.name, self.code)
    
    def has_requirements(self):
        return    self.required_full_desc or self.required_brief_desc\
               or self.required_meta_info or self.required_images_count >0\
               or  False

    def save(self, *args, **kwargs):
        self.sync = True
        return super(Product, self).save(*args, **kwargs)

    def check_requirements(self):
        """Checks requirements to match
           returns true if product matches all requirements
        """
        if self.required_full_desc and not self.full_desc:
            return False
        if self.required_brief_desc and not self.brief_desc:
            return False
        if self.required_meta_info and not (self.meta_title and self.meta_keywords and self.meta_descriptions):
            return False
        if self.required_images_count > self.photos.count():
            return False
        return True

class Photo(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, related_name = 'photos')
    position = models.IntegerField("Позиция", blank=True, default = 1)
    to_del = models.BooleanField(default=False)
    image = models.ImageField("Фотография", upload_to='photos', blank=True)

    def save(self, *args, **kwargs):
        if self.product:
           self.product.sync = True
           self.product.save()
        return super(Photo, self).save(*args, **kwargs)

