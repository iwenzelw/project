from django.conf.urls import url
from django.conf import settings
from django.urls import re_path
from . import views

# re_path(r'^comments/(?:page-(?P<page_number>\d+)/)?$', comments),  # good

urlpatterns = [
    #path('add_blog', views.add_blog, name='add_blog'),
    #re_path(r'^edit/blog/((?P<id>\d+)/$', views.edit_blog, name='edit_blog'),
    #re_path(r'^blog/((?P<id>\d+)/$', views.blog, name='blog'),
    url(r'^add/blog/$', views.add_blog, name='add_blog'),
    url(r'^edit/blog/(?P<id>\d+)/$', views.edit_blog, name='edit_blog'),
    url(r'^blog/(?P<id>\d+)/$', views.blog, name='blog'),  # < 1
]