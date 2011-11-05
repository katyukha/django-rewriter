# Create your views here.
from django.http import HttpResponce
from django_rewriter.product.form import ProductForm

def view_form(request):
    f = ProductForm(request.POST)
    new_product = f.save()

