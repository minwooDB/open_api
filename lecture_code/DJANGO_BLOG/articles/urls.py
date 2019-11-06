from django.urls import path
from . import views

app_name = 'articles'


urlpatterns = [
    path('delete/<int:article_id>/',views.delete, name = 'delete'),
    path('edit/<int:article_id>/', views.edit, name = 'edit'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('create/', views.create, name = 'create'),
    path('comments/<int:article_id>/', views.comment_create, name='comment_create'),
    path('comments/<int:article_id>/delete/<int:comment_id>/',views.comment_delete,name='comment_delete'),
    # path('new/', views.new),
    path('', views.index, name = 'index'),
]