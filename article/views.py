from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from datetime import datetime
from article.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth


def index(request):
    #nav = Navigation.objects.all()
    #news=News.objects.all()
    #firstnews=news[0]
    #context = { 'nav' : nav, 'firstnews':firstnews}
    context = {}
    return render_to_response ('index.html', context, context_instance = RequestContext(request))

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            if not request.POST.get('remember_me', None):
                request.session.set_expiry(0)
            return HttpResponseRedirect(reverse('index'))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
#def register(request):
    