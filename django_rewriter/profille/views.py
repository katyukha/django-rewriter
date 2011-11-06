from django_rewriter.product.models import UserProfile
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def profile(request, template_name = 'profile/profile.html'):
	return render_to_response(template_name, {},
	                  context_instance = RequestContext(request))
