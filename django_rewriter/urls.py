from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# import form class
from profille.auth import RegistrationFormExtraInfo

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^profile/',      include('profille.urls')),

    url(r'^product/',      include('product.urls')),

    url(r'^registration/complete/$', 'django.views.generic.simple.direct_to_template', 
                           {'template' : 'registration/registration_complete.html'},
                           name = 'registration_complete'),
    url(r'^registration/register/$',
                           'registration.views.register',
                           { 'backend': 'profille.auth.InactiveProfileRegisterBackend',
                             'success_url' : 'registration_complete',
                             'form_class' : RegistrationFormExtraInfo,},
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
