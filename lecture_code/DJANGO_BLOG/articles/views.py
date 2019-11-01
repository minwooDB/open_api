from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.order_by('-pk')
    #articles = Article.objects.all()[::-1]
    return render(request, 'articles/index.html', {'articles':articles})

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        # 1.
        # article = Article()
        # article.title = title
        # article.content =content
        # article.save()
        # 2.
        # article = Article(title = title, content=content)
        # article.save()

        # 3.andArticle.objects.create(title = title, content=content)

        #return render(request, 'articles/create.html')
        return redirect(f'/articles/{article.pk}')
    else : 
        return render(request,'articles/new.html')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/detail.html',{'article':article})

def edit(request, pk):
    if request.method=='POST':
        article = Article.objects.get(pk=pk)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect(f'/articles/{article.pk}')
    else:
        article = Article.objects.get(pk=pk)
        return render(request,'articles/edit.html',{'article':article})

def delete(request,pk):
    article= Article.objects.get(pk=pk)
    article.delete()
    return redirect("/articles/")
