from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='the_main-home'),
    path('rental', views.rental, name='the_main-rental'),
    path('apartment', views.apartment, name='the_main-apartment'),
    path('contacti', views.contacti, name='the_main-contacti'),
    path('site', views.site, name='the_main-site'),

]
