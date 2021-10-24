from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


#@login_required(login_url='/login')
def index(request):
    contex={
        'users':User.objects.all()

    }
    return render(request,"index.html",contex)