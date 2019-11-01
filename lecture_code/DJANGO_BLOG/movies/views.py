from django.shortcuts import render, redirect
from .models import movie

def index(request):
    #movie = movie.objects.order_by('open_date')
    Movies = movie.objects.all()[::-1]
    return render(request, 'movies/index.html', {'Movies':Movies})

def new(request):
    if request.method=='POST':
        title = request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience =  request.POST.get('audience')
        open_date =  request.POST.get('open_date')
        genre =  request.POST.get('genre')
        watch_grade =  request.POST.get('watch_grade')
        score =  request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description =  request.POST.get('description')
        Movie = movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, 
                    watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
        Movie.save()
        return redirect('/movies/')
    else : 
        return render(request,'movies/new.html')

def detail(request, pk):
    Movie = movie.objects.get(pk=pk)
    return render(request, 'movies/detail.html',{'Movie':Movie})

def edit(request, pk):
    if request.method=='POST':
        Movie = movie.objects.get(pk=pk)
        Movie.title = request.POST.get('title')
        Movie.title_en = request.POST.get('title_en')
        Movie.audience =  request.POST.get('audience')
        Movie.open_date =  request.POST.get('open_date')
        Movie.genre =  request.POST.get('genre')
        Movie.watch_grade =  request.POST.get('watch_grade')
        Movie.score =  request.POST.get('score')
        Movie.poster_url = request.POST.get('poster_url')
        Movie.description =  request.POST.get('description')
        Movie.save()
        return redirect(f'/movies/{Movie.pk}')
    else:
        Movie = movie.objects.get(pk=pk)
        return render(request,'movies/edit.html',{'Movie':Movie})


def delete(request,pk):
    Movie = movie.objects.get(pk=pk)
    Movie.delete()
    return redirect("/movies/")

