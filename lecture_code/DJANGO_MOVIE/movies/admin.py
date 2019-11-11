from django.contrib import admin
from .models import Genre, Movie, Score

class GenreAdmin(admin.ModelAdmin):
   admin.site.register(Genre)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'audience', 'poster_url', 'description', 'genre_id')

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id','content','score','movie_id')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Score, ScoreAdmin)