from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('score/<int:movie_id>/',views.score_new, name= 'score_new'),
    path('<int:movie_id>/delete/<int:score_id>/',views.score_delete, name= 'score_delete'),
    path('delete/<int:movie_id>/',views.delete, name= 'delete'),
    path('new/',views.new),
    path('<int:movie_id>/', views.detail, name= 'detail'),
    path('edit/<int:movie_id>/', views.edit, name = 'edit'),
    path('', views.index),
]