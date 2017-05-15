from django.shortcuts import render,redirect
from .models import Item
from ..main_app.models import Wishlist
from ..logreg.models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'item/index.html')

def additem(request):
    response_from_models = Item.objects.addItem(request.POST,request.session['user_id'])
    
    if response_from_models['status']:
        print "successfully added item", response_from_models['item']
        user = User.objects.get(id = request.session['user_id'])
        Wishlist.objects.addListItem(response_from_models['item'].id, user)
        return redirect('main:wishlist')
    else:
        for error in response_from_models['errors']:
            messages.error(request, error)
        return redirect('item:index')

def deleteitem(request,id):
    Item.objects.get(id = id).delete()
    return redirect('main:wishlist')
