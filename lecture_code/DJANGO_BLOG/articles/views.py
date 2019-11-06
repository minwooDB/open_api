from django.shortcuts import render, redirect
from .models import Article, Comment

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
        image = request.FILES.get('image')
        article = Article(title=title, content=content, image = image)
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

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    comments = article.comment_set.all()
    return render(request, 'articles/detail.html',{'article':article,'comments':comments})

def edit(request, article_id):
    if request.method=='POST':
        article = Article.objects.get(pk=article_id)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        image = request.FILES.get('image')
        article.save()
        return redirect(f'/articles/{article.pk}')
    else:
        article = Article.objects.get(pk=pk)
        return render(request,'articles/edit.html',{'article':article})

def delete(request,article_id):
    article= Article.objects.get(pk=article_id)
    article.delete()
    return redirect("/articles/")

def comment_create(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method =='POST':
        comment = Comment()
        comment.content = request.POST.get('content')
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.id)
    else:
        return redirect('articles:detail', article.id)

def comment_delete(request,comment_id,article_id):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_id)
        comment.delete()
    return redirect('articles:detail',article_id)

