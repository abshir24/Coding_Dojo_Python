from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User
# Create your models here.

class ItemManager(models.Manager):
    def addItem(self,postData,user_id):
        errors = []
        if not len(postData['new_item']):
            errors.append('I cannot accept any empty entries')

        if len(postData['new_item']) < 3:
            errors.append('Your entry has to be at least 3 characters long')

        response_to_views ={}

        if errors:
            response_to_views['status'] = False
            response_to_views['errors'] = errors
        else:
            print "user_id",user_id
            this_creator = User.objects.get(id = user_id)
            item = self.create(item = postData['new_item'], user = this_creator)
            response_to_views['status'] = True
            response_to_views['item'] = item

        return response_to_views


class Item(models.Model):
    item = models.CharField(max_length = 45)
    user = models.ForeignKey(User, related_name = 'created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ItemManager()
