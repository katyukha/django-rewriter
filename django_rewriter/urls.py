from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^profile/',      include('profille.urls')),

    url(r'^product/',      include('product.urls')),

    url(r'^registration/register/$',
                           'registration.views.register',
                           { 'backend': 'registration.backends.simple.SimpleBackend',
                             'success_url' : 'profile',},
                           name='registration_register'),
                           
    url(r'^registration/logout/$', 
                           'django.contrib.auth.views.logout',
                           { 'next_page' : '/'},
                           name='auth_logout'),
    url(r'^registration/', include('registration.backends.simple.urls')),

    url(r'^$',             'profille.views.profileuser', name = 'home'),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # Examples:
    # url(r'^$', 'django_rewriter.views.home', name='home'),
    # url(r'^django_rewriter/', include('django_rewriter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
