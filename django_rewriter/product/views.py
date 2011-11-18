# Create your views here.
from django.template import RequestContext
from django_rewriter.product.models import Product
from django_rewriter.product.form import ProductForm
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def product_list(request, status = None, owners_only = False, template_name = "product/list.html"):
    ls = Product.objects.all()
    if status:
       ls = ls.filter(status = status)
    if owners_only:
       ls = ls.filter(user = request.user)
    return render_to_response(template_name, {
              'product_list' : ls,
              'owners_only'  : owners_only,
              'current_path' : request.path,
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
        form = ProductForm(request.user.profile, instance = p)
    return render_to_response(template_name,{
                'form':form,
                'prod':p,
                }, context_instance=RequestContext(request))

@login_required
def linking(request, product_id):
    p = get_object_or_404(Product, pk=product_id)
    p.user = request.user
    p.status = 'progress'
    p.save()
    next_page = request.GET.get('next_page')
    if next_page:
        return redirect(next_page)
    else:
        return redirect("product_view", product_id = product_id)

@login_required
def product_view(request, product_id, template_name = "product/view.html"):
    p = get_object_or_404(Product, pk=product_id)
    return render_to_response(template_name,{
                'prod':p,
                }, context_instance=RequestContext(request))

@login_required
def product_send(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.user != request.user:  # if somebody trye to send not own product
       raise Http404
    product.status = 'done'
    product.save()
    return redirect("product_view", product_id = product_id)
    

