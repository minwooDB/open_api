from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('peoples/', include('peoples.urls')),
    path('articles/', include('articles.urls')),
    path('students/', include('students.urls')),
    path('admin/', admin.site.urls),
]
