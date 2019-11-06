from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}. 장르:{self.name}' 

class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}.{self.title}:{self.content}'


class Score(models.Model):
     content = models.CharField(max_length=140)
     score = models.IntegerField()
     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
        
     def __str__(self):
        return f'{self.id}.{self.score}:{self.movie_id}'
     