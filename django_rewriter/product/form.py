from django.forms import ModelForm
from django_rewriter.product.models import Product

class ProductForm(ModelForm):

    def __init__(self, user_profile, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id and not user_profile.is_seo:
            self.fields['meta_title'].widget.attrs['readonly'] = True
            self.fields['meta_keywords'].widget.attrs['readonly'] = True
            self.fields['meta_desc'].widget.attrs['readonly'] = True

    class Meta:
        model = Product
        exclude = ('user', 'status', 'rating')
