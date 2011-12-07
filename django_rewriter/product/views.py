# Create your views here.
from django.template import RequestContext
from django_rewriter.product.models import Product, Photo
from django_rewriter.product.form import ProductForm, PhotoForm
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
              'product_list'  : ls,
              'owners_only'   : owners_only,
              'current_path'  : request.path,
              'filter_status' : status,
              }, context_instance=RequestContext(request))

@login_required
def add_product(request, template_name = "product/add.html"):
    if request.method == 'POST':
        form = ProductForm(request.user.profile, request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(request.user.profile)
    return render_to_response(template_name,{
                'form':form,
                }, context_instance=RequestContext(request))

@login_required
def product_edit(request, product_id, template_name = "product/edit.html"):
    p = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.user.profile, p, request.POST, instance = p)
        if form.is_valid():
            form.save()
        return redirect("product_view", product_id = product_id)        
    else:
        form = ProductForm(request.user.profile, p, instance = p)
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
    photos = Photo.objects.all().filter(product=product_id)
    ls = list(photos)
    for i in range(len(ls)-1):
        for j in range(len(ls)-1):
            if ls[j].position > ls[j+1].position:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return render_to_response(template_name,{
                'prod':p,
                'photos':ls,
                'len':len(ls),
                }, context_instance=RequestContext(request))

@login_required
def product_send(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.user != request.user:  # if somebody tryes to send not own product
       raise Http404
    product.status = 'done'
    product.save()
    return redirect("product_view", product_id = product_id)

@login_required
def photo_add(request, product_id, template_name = "product/add_photo.html"):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = PhotoForm(True, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_view", product_id = product_id)
    else:
        form = PhotoForm(True, {'product':product_id})

    return render_to_response(template_name,{
                'form':form,
                'product':product,
                }, context_instance=RequestContext(request))

@login_required
def photo_edit(request, product_id, photo_id, template_name = "product/edit_photo.html"):
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.method == 'POST':
        form = PhotoForm(False, request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            if photo.to_del:
                photo.delete()
            return redirect("product_view", product_id = product_id)
    else:
        form = PhotoForm(False, instance=photo)

    return render_to_response(template_name,{
                'form':form,
                'photo':photo,
                'product':photo.product
                }, context_instance=RequestContext(request))
