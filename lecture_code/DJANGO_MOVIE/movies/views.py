from django.shortcuts import render, redirect
from .models import Movie, Score

def index(request):
    #movie = movie.objects.order_by('open_date')
    movies = Movie.objects.all()[::-1]
    return render(request, 'movies/index.html', {'movies':movies})

def new(request):
    if request.method=='POST':
        title = request.POST.get('title')
        audience =  request.POST.get('audience')
        poster_url = request.POST.get('poster_url')
        description =  request.POST.get('description')
        genre_id = request.POST.get('genre_id')
        movie = Movie(title=title, audience=audience, poster_url=poster_url, description=description) 
        movie.save()
        return redirect('/movies/')
    else : 
        return render(request,'movies/new.html')
#detail 다시보기
def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    scores = movie.score_set.all()
    return render(request, 'movies/detail.html',{'movie':movie, 'scores':scores})

def edit(request, movie_id):
    if request.method=='POST':
        movie = Movie.objects.get(pk=movie_id)
        movie.title = request.POST.get('title')
        movie.audience =  request.POST.get('audience')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        genre_id = request.POST.get('genre_id')
        movie.save()
        return redirect(f'/movies/{movie.pk}')
    else:
        movie = Movie.objects.get(pk=movie_id)
        return render(request,'movies/edit.html',{'movie':movie})


def delete(request,movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie.delete()

def score_new(request, movie_id):
    movie = Movie.objects.get(pk= movie_id)
    if request.method =='POST':
        score = Score()
        score.content = request.POST.get('content')
        score.score = request.POST.get('score')
        score.movie_id = movie
        score.save()
        return redirect('movies:detail', movie_id)
    else:
        return redirect('movies:detail', movie_id)

def score_delete(request, movie_id, score_id):
    if request.method == 'POST':
        score = Score.objects.get(pk=score_id)
        score.delete()
    return redirect('movies:detail',movie_id)

