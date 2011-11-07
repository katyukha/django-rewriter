from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^profile/$', 'django_rewriter.profille.views.profileuser'),
    url(r'^accounts/$', include('registration.backends.simple.urls')),
    url(r'^list/$', 'django_rewriter.product.views.product_list'),
    url(r'^add/$', 'django_rewriter.product.views.add_product'),
    url(r'^(?P<product_id>\d+)/$', 'django_rewriter.product.views.product_view', name = 'product_view'),
    url(r'^edit/(?P<product_id>\d+)/$', 'django_rewriter.product.views.edit', name = 'product_edit'),
    url(r'^edit/(?P<product_id>\d+)/connect/', 'django_rewriter.product.views.linking', name = 'product_linking'),
    url(r'^profile/', 'django_rewriter.profille.views.profileuser'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^list/', 'django_rewriter.product.views.product_list'),
    url(r'^add/', 'django_rewriter.product.views.add_product'),
    url(r'^(?P<product_id>\d+)/', 'django_rewriter.product.views.product_view'),
    #url(r'^(?P<username>\w+)/edit/', 'django_rewriter.profille.views.edit', name = 'user_edit'),
    #url(r'^/', 'django_rewriter.product.views.add_product'),
    # Examples:
    # url(r'^$', 'django_rewriter.views.home', name='home'),
    # url(r'^django_rewriter/', include('django_rewriter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
