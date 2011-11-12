from django_rewriter.profille.models import UserProfile
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django_rewriter.form import ProfileForm2, ProfileForm
from django.shortcuts import get_object_or_404
from django_rewriter.product.models import Product

@login_required
def profileuser(request, template_name = 'profille/profile.html'):
    ls = Product.objects.all()
    return render_to_response(template_name, {
                'product_list': ls
                 }, context_instance = RequestContext(request))


def edit(request, username, template_name = "profille/edit.html"):
    p = get_object_or_404(User, username = username)
    if request.method == 'POST':
        form = ProfileForm2(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/profile/")
    else:
        u = p.get_profile()
        p.first_name = form.first_name
        FormDate = {
	        'f_name':u.first_name,
	        'l_name':u.last_name,
	        'url':'http://',
	        'UserInfo':'UserInfo',
		}
        form = ProfileForm2(initial = FormDate)
    return render_to_response(template_name,{
        'form':form,
        'username':username,
         }, context_instance=RequestContext(request))
