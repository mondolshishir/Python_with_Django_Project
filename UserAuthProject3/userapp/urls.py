#from django.conf.urls import urls
from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register')
]
