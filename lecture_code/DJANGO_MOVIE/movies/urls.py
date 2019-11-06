from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:pk>/',views.delete),
    path('new/',views.new),
    path('<int:pk>/', views.detail),
    path('edit/<int:pk>/', views.edit),
    #path('create/',views.create),
    path('', views.index),
]