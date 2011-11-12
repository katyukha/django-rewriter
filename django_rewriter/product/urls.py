from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('product.views',
    url(r'^list/$',                             'product_list',  name='product_list'),
    url(r'^add/$',                              'add_product',   name='product_add'),
    url(r'^(?P<product_id>\d+)/$',              'product_view',  name = 'product_view'),
    url(r'^(?P<product_id>\d+)/edit/$',         'edit',          name = 'product_edit'),
    url(r'^(?P<product_id>\d+)/edit/connect/$', 'linking',       name = 'product_linking'),
)
