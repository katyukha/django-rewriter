from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('profille.views',
    url(r'^$',          'profileuser',  name = 'profile'),
    url(r'^edit/$',     'edit',         name = 'profile_edit'),
)    
