# -*- coding:utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from profille.form import ProfileForm
from product.models import Product

@login_required
def profileuser(request, template_name = 'profille/profile.html'):
    products = Product.objects.filter(user=request.user)
    return render_to_response(template_name, {
                'product_list': products,
                 }, context_instance = RequestContext(request))

@login_required
def edit(request, template_name = "profille/edit.html"):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name   = form.cleaned_data['f_name']
            user.last_name    = form.cleaned_data['l_name']
            profile.phone     = form.cleaned_data['phone']
            user.save()
            profile.save()
            return redirect("profile")
    else:
        FormData = {
            'f_name'    : user.first_name,
            'l_name'    : user.last_name,
            'phone'     : profile.phone,
        }
        form = ProfileForm(initial = FormData)
    return render_to_response(template_name,{
        'form':form,
         }, context_instance=RequestContext(request))
