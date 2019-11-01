from django.urls import path
from . import views


urlpatterns = [
    path('delete/<int:pk>/',views.delete),
    path('edit/<int:pk>/', views.edit),
    path('<int:pk>/', views.detail),
    path('create/', views.create),
    # path('new/', views.new),
    path('', views.index),
]