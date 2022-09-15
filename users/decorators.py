from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
import functools





def user_consented(view_func, redirect_url='profile'):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.userconsent.consent:
            print(f"USER -{request.user}- CONSENTED")
            return view_func(request, *args, **kwargs)
        print(f"{request.user} NO CONSENTO")
        messages.warning(request, _('You must consent to the terms of this research project before you can do that!'))
        return redirect(redirect_url)
    return wrapper
