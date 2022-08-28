#from django.conf.urls import url
from django.urls import path
from . import views

app_name= "first_app"


urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    #path('test/', views.contact, name = 'contact'),
]