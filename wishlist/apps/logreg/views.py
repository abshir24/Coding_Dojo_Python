from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
from ..main_app.models import Wishlist

# Create your views here.

def index(request):
    context = {
    }
    return render(request,'logreg/index.html',context)

def login(request):
    response_from_models = User.objects.login_user(request.POST)

    if response_from_models['status']:
        request.session['user_id'] = response_from_models['user'].id
        return redirect('main:wishlist')
    else:
        messages.error(request, response_from_models['errors'])
        return redirect('logreg:index')


def register(request):
    response_from_models = User.objects.register_user(request.POST)

    if response_from_models['status']:
        request.session['user_id'] = response_from_models['user'].id
        addlist = Wishlist.objects.addList(request.session['user_id'])
        return redirect('main:wishlist')
    else:
        for error in response_from_models['errors']:
            messages.error(request, error)

        return redirect('logreg:index')

def logout(request):
    request.session.clear()
    return redirect('logreg:index')
