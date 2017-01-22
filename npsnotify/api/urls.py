from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^send/', views.sendmsg.as_view(), name='sendmsg'),
    url(r'^details/', views.details.as_view(), name='details'),
    url(r'^getgroups/', views.getgroups.as_view(), name='getgroups'),
]
