from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sendmsg.as_view(), name='sendmsg'),
]
