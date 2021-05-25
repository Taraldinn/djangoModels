from django.conf.urls import url
from django.urls import path
from appone import views

app_name = "appone"
urlpatterns =[
    path('', views.index, name='index'),
    path('form/', views.form, name='form')
]
