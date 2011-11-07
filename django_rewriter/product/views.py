# Create your views here.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django_rewriter.product.models import Product
from django_rewriter.product.form import ProductForm
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404


def product_list(request, template_name = "product/list.html"):
    ls = Product.objects.all()
    return render_to_response(template_name, {
              'product_list' : ls,
              }, context_instance=RequestContext(request))
def add_product(request, template_name = "product/add.html"):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/list/")
    else:
        form = ProductForm()

    return render_to_response(template_name,{
                'form':form,
                }, context_instance=RequestContext(request))
def edit(request, product_id, template_name = "product/edit.html"):
    p = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance = p)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/list/")
    else:
        form = ProductForm(instance = p)
    return render_to_response(template_name,{
                'form':form,
                'prod':p,
                }, context_instance=RequestContext(request))
def linking(request, product_id, template_name = 'product/edit.html'):
    p = get_object_or_404(Product, pk=product_id)
    #p.user = request.user
    p.status = 'during'
    p.save()
    form = ProductForm(instance = p)
    return render_to_response(template_name,{
                'form':form,
                'prod':p,
                }, context_instance=RequestContext(request))

def product_view(request, product_id, template_name = "product/view.html"):
    p = get_object_or_404(Product, pk=product_id)
    return render_to_response(template_name,{
                'prod':p,
                }, context_instance=RequestContext(request))
    