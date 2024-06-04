from pprint import pprint

from django import template
from articles.models import *
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy

register = template.Library()

@register.simple_tag(name='get_cats')
def get_catigories():
    # return Category.objects.all()
    # pprint(Articles.objects.values('cat_id').annotate(ww=Count('id')))
    return Category.objects.annotate(total=Count('articles')).filter(total__gt=0).order_by('id')
# https://youtu.be/QrO-YgfWAOU?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&t=2795


from main.forms import RegisterUserForm, LoginUserForm
from main.views import Register, Login

@register.simple_tag(name='get_reg_form')
def get_registration_form(request):
    if (request.method == "POST") and ('password2' in request.POST):
        form = RegisterUserForm(request.POST)
        # print(form)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return {'refresh': 1}
                # return redirect('feedback')
                # print("**",request.META.get('HTTP_REFERER'))
                # return request.META.get('HTTP_REFERER')
            except:
                form.add_error(None,'Form didn`t save!!!')
        else:
            HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return {'form': form, 'open':1}
    return {'form': RegisterUserForm, 'open':0}


# # or
# @register.inclusion_tag('main/layout.html')
# def show_catigories():
#     return {'cat': Category.objects.all()}



from django.contrib.auth import authenticate, login

@register.simple_tag(name='get_log_form')
def get_login_form(request):
    if request.method == 'POST' and ('password' in request.POST):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return {'refresh': 1 }
            # return reverse_lazy('home')
        else:
            return {'form': LoginUserForm(request.POST), 'open': 1}
    return {'form': LoginUserForm}