from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('static_example/', views.static_example),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('ispal2/', views.ispal2),
    path('input_word/', views.input_word),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('ispal/<word>', views.ispal),
    path('isbirth/', views.isbirth),
    path('image/', views.image),
    path('template_language/',views.template_language),
    path('area/<int:width>/<int:height>/',views.square),
    path('introduce/<name>/<int:age>/',views.introduce),
    path('hello/<name>/',views.hello),
    path('lotto2/', views.lotto2),
    path('lotto/', views.lotto),
    path('dinner/', views.dinner),
    path('hola/', views.hola),
    path('index/', views.index),
]