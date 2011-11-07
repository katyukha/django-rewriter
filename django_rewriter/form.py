from django.forms import ModelForm
from django_rewriter.product.models import UserProfile

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
