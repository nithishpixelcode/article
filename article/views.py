from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from datetime import datetime
from article.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def index(request):
    #nav = Navigation.objects.all()
    #news=News.objects.all()
    #firstnews=news[0]
    #context = { 'nav' : nav, 'firstnews':firstnews}
    context = {}
    return render_to_response ('index.html', context, context_instance = RequestContext(request))
