from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User
# Create your models here.

class SecretManager(models.Manager):
    def validateSecret(self,postData, user_id):
        errors = []
        if not len(postData['secret']):
            errors.append('Please add something to your secret post')

        response_to_views ={}

        if errors:
            response_to_views['status'] = False
            response_to_views['errors'] = errors
        else:
            print "user_id",user_id
            this_creator = User.objects.get(id = user_id)
            secret = self.create(secret = postData['secret'], user = this_creator )
            response_to_views['status'] = True
            response_to_views['secret'] = secret

        return response_to_views

    def validateLike(self,user_id,secret_id):
        response_to_views ={}
        user = User.objects.get(id = user_id)
        print user.id
        secret = Secret.objects.get(id = secret_id)
        print secret.id
        if user in secret.likes.all() :
            print "inside like condition"
            response_to_views['status'] = False
        else:
            print "inside else condition"
            this_secret = Secret.objects.get(id = secret_id)
            this_liker = User.objects.get(id = user_id)
            this_secret.likes.add(this_liker)
            response_to_views['status'] = True
            
        return response_to_views


class Secret(models.Model):
    secret = models.CharField(max_length = 45)
    likes = models.ManyToManyField(User,related_name = "likes")
    user = models.ForeignKey(User, related_name = 'created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = SecretManager()
