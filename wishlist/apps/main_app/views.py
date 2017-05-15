from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from ..logreg.models import User
from ..main_app.models import Wishlist
from ..item.models import Item
# Create your views here.

def wishlist(request):
    my_wishlists = Wishlist.objects.filter(user = User.objects.filter(id = request.session['user_id']))
    my_items = []
    
    context = {
        "MyWishlist": Wishlist.objects.filter(user = User.objects.filter(id = request.session['user_id'])),
        "user":User.objects.filter(id = request.session['user_id']),
        "all_wishlists": Wishlist.objects.exclude(user = User.objects.get(id = request.session['user_id'])),
        "my_items": my_items,
    }
    return render(request,'main_app/index.html', context)

def addItem(request,id):
    user = User.objects.get(id = request.session['user_id'])
    Wishlist.objects.addListItem(id,user)
    return redirect('main:wishlist')
