from django.forms import ModelForm
from django_rewriter.product.models import Product
from django.forms.widgets import HiddenInput

class ProductForm(ModelForm):

    def __init__(self, user_profile, prod, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        if not prod.required_full_desc:
            self.fields['full_desc'].widget = HiddenInput()
        if not prod.required_brief_desc:
            self.fields['brief_desc'].widget = HiddenInput()
        if not prod.required_meta_info or not user_profile.is_seo:
            self.fields['meta_title'].widget = HiddenInput()
            self.fields['meta_desc'].widget = HiddenInput()
            self.fields['meta_keywords'].widget = HiddenInput()

    class Meta:
        model = Product
        exclude = ( 'user', 'status', 'rating', 'required_full_desc',
                    'required_brief_desc', 'required_meta_info',
                    'required_images_count', 'sync')
