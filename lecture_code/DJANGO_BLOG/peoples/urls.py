from django.urls import path
from . import views


urlpatterns = [
    path('delete/<int:pk>/',views.delete),
    path('create/',views.create),
    path('', views.index),
]