from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login/$', views.login_),
    re_path(r'^logout/$', views.logout_),
    re_path(r'^registration/$', views.registration_),
    re_path(r'^about/$', views.about),
    re_path(r'^feedback/$', views.comment),
    re_path(r'^work/$', views.work)
]