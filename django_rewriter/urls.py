from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
'''<<<<<<< HEAD
# TODO : review urls. remove old, make them more readable.
#<<<<<<< HEAD
    url(r'^profile/$', 'django_rewriter.profille.views.profileuser', name = 'profile'),
    url(r'^(?P<username>\w+)/edit/$', 'django_rewriter.profille.views.edit', name = 'user_edit'),
    url(r'^profile/$', 'django_rewriter.profille.views.profileuser'),
    
    url(r'^list/$', 'django_rewriter.product.views.product_list', name='product_list'),
    url(r'^add/$', 'django_rewriter.product.views.add_product'),
    url(r'^(?P<product_id>\d+)/$', 'django_rewriter.product.views.product_view', name = 'product_view'),
    url(r'^edit/(?P<product_id>\d+)/$', 'django_rewriter.product.views.edit', name = 'product_edit'),
    url(r'^edit/(?P<product_id>\d+)/connect/$', 'django_rewriter.product.views.linking', name = 'product_linking'),
    
    url(r'^list/$', 'django_rewriter.product.views.product_list'),
    url(r'^add/$', 'django_rewriter.product.views.add_product'),
    url(r'^(?P<product_id>\d+)/$', 'django_rewriter.product.views.product_view'),
  
    url(r'^', include('registration.backends.simple.urls')),
    url(r'^$', 'django_rewriter.profille.views.profileuser'),
#=======
    #url(r'^(?P<product_id>\d+)/$', 'django_rewriter.product.views.product_view', name = 'product_view'),
    #url(r'^edit/(?P<product_id>\d+)/$', 'django_rewriter.product.views.edit', name = 'product_edit'),
    #url(r'^(?P<product_id>\d+)/connect/$', 'django_rewriter.product.views.linking', name = 'product_linking'),
    #url(r'^profile/$', 'django_rewriter.profille.views.profileuser'),
    #url(r'^', include('registration.backends.simple.urls')),
    #url(r'^list/$', 'django_rewriter.product.views.product_list'),
    #url(r'^add/$', 'django_rewriter.product.views.add_product'),
    #url(r'^(?P<product_id>\d+)/$', 'django_rewriter.product.views.product_view'),
    #url(r'^$', 'django_rewriter.profille.views.profileuser'),
    #url(r'^(?P<username>\w+)/edit/$', 'django_rewriter.profille.views.edit', name = 'user_edit'),
#>>>>>>> dda843a12ca3a4992038182053ba8ca0b5574fd3
======='''

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

#>>>>>>> 0cc22adbd16b35627dcf2c2e7529fd0e877e6605
    # Examples:
    # url(r'^$', 'django_rewriter.views.home', name='home'),
    # url(r'^django_rewriter/', include('django_rewriter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
