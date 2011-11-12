from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('profille.views',
    url(r'^$',                        'profileuser', name = 'profile'),
    url(r'^(?P<username>\w+)/edit/$', 'edit',        name = 'user_edit'),
)    
