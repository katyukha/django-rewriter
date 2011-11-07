from django_rewriter.profille.models import UserProfile
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def profileuser(request, template_name = 'profille/profile.html'):
	return render_to_response(template_name, {},
	                  context_instance = RequestContext(request))

'''def edit(request, username, template_name = "user/edit.html"):
    p = get_object_or_404(User, username = username)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance = p)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/profile/")
    else:
        form = ProfileForm(instance = p)
    return render_to_response(template_name,{
                'form':form,
                'user':username,
                }, context_instance=RequestContext(request))'''
