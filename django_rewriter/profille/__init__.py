from registration.backends.simple import SimpleBackend
from django.contrib.auth.models import User
from registration import signals

class InactiveSimpleBackend(SimpleBackend):
     def register(self, request, **kwargs):
        """
        Create and immediately log in a new user.

        """
        username, email, password = kwargs['username'], kwargs['email'], kwargs['password1']
        new_user = User.objects.create_user(username, email, password)
        new_user.is_active = False
        new_user.save()

        # authenticate() always has to be called before login(), and
        # will return the user we just created.
        #new_user = authenticate(username=username, password=password)
        #login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

