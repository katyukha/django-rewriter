# Create your views here.
from django.template import RequestContext
from django_rewriter.product.models import Product
from django_rewriter.product.form import ProductForm
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def product_list(request, status = None, owners_only = False, template_name = "product/list.html"):
    ls = Product.objects.all()
    if status:
       ls = ls.filter(status = status)
    if owners_only:
       ls = ls.filter(user = request.user)
    return render_to_response(template_name, {
              'product_list' : ls,
              }, context_instance=RequestContext(request))

@login_required
def add_product(request, template_name = "product/add.html"):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render_to_response(template_name,{
                'form':form,
                }, context_instance=RequestContext(request))

@login_required
def edit(request, product_id, template_name = "product/edit.html"):
    p = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance = p)
        if form.is_valid():
            form.save()
        return redirect("product_view", product_id = product_id)        
    else:
        form = ProductForm(instance = p)
    return render_to_response(template_name,{
                'form':form,
                'prod':p,
                }, context_instance=RequestContext(request))

@login_required
def linking(request, product_id, template_name = 'product/list.html'):
    all = Product.objects.all()
    p = get_object_or_404(Product, pk=product_id)
    p.user = request.user
    p.status = 'during'
    p.save()
    return render_to_response(template_name,{
                'product_list':all,
                }, context_instance=RequestContext(request))

@login_required
def product_view(request, product_id, template_name = "product/view.html"):
    p = get_object_or_404(Product, pk=product_id)
    return render_to_response(template_name,{
                'prod':p,
                }, context_instance=RequestContext(request))
    
