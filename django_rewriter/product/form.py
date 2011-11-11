from django.forms import ModelForm
from django_rewriter.product.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('user','status')
