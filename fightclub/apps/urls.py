from django.urls import path, include
from . import views


urlpatterns = [

    path('',views.index, name='index'),
    path('login',views.login,name='login'),
    path('registro',views.registro, name='registro'),
    path('logout', views.logout , name='logout'),
    path('jugar',views.jugar, name = 'jugar'),
    path('jugar2',views.jugar2, name = 'jugar2'),
    path('index2',views.index2, name = 'index2'),
    path('registro2',views.registro2, name='registro2'),
    ]


