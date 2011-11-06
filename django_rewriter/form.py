from django.forms import ModelForm
from django_rewriter.product.models import UserProfile

class ProductForm(ModelForm):
    class Meta:
        model = UserProfile
