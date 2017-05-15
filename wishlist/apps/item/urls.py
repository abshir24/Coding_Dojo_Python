from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^additem$', views.additem, name = 'additem'),
    url(r'^(?P<id>\d+)/delete$', views.deleteitem, name = 'delete')
]
