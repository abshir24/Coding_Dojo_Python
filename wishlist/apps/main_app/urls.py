from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^wishlist$', views.wishlist, name = 'wishlist'),
    url(r'^(?P<id>\d+)/additem$', views.addItem, name = 'additem')
]
