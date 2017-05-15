from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User
from ..item.models import Item
# Create your models here.

class WishlistManager(models.Manager):
    def addList(self,user_id):
        print "user_id",user_id
        this_creator = User.objects.get(id = user_id)
        return self.create(user = this_creator )

    def addListItem(self,item_id,user):
        print "item_id", item_id
        item = Item.objects.get(id = item_id)
        print "item.id",item.id
        wishlist = Wishlist.objects.get(user = user)
        print wishlist.id
        wishlist.items.add(item)
        print "success"
        return

class Wishlist(models.Model):
    items = models.ManyToManyField(Item,related_name = "items")
    user = models.OneToOneField(User,related_name = "wishlist")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = WishlistManager()
