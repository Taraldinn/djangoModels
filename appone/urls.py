from django.conf.urls import url
from django.urls import path
from appone import views

urlpatterns =[
    path('', views.index, name='index')
]
