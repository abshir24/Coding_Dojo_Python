from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^secrets$', views.secrets, name = 'secrets'),
    url(r'^addSecret$', views.addSecret, name = 'addsecret'),
    url(r'^(?P<id>\d+)/addLike$', views.addLike, name = 'addlike'),
    url(r'^allsecrets$', views.allsecrets, name = 'allsecrets'),
    url(r'^(?P<id>\d+)/delete$', views.deletesecret, name = 'delete')
]
