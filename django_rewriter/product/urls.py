from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('product.views',
    url(r'^list/(?P<status>\w+)?$',             'product_list',  name='product_list'),
    url(r'^my-list/(?P<status>\w+)?$$',         'product_list',  name='product_my_list', 
                                                                 kwargs = {'owners_only':True}),
    url(r'^add/$',                              'add_product',   name='product_add'),
    url(r'^(?P<product_id>\d+)/$',              'product_view',  name = 'product_view'),
    url(r'^(?P<product_id>\d+)/edit/$',         'edit',          name = 'product_edit'),
    url(r'^(?P<product_id>\d+)/send/$',         'product_send',  name = 'product_send'),
    url(r'^(?P<product_id>\d+)/edit/connect/$', 'linking',       name = 'product_linking'),
)
