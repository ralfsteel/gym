from django.shortcuts import render
from django.http import HttpResponse
from mygym.models import Training
from django.template import RequestContext, loader
from django.contrib.auth.models import User

import datetime
# Create your views here.

def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'mygym/index.html', context)


def detail(request, _id):
    user = User.objects.get(pk=_id)
    now = datetime.datetime.now()
    context = {
        'user': user,
        'now': now
    }
    return render(request, 'mygym/detail.html', context)
