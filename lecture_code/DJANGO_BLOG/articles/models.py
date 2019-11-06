from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
    # ProcessedImageField(
    #     upload_to = 'articles/images', # 저장 위치(MEDIA_ROOT/articles/images)
    #     processors = [Thumbnail(200,300)], # 처리할 작업 목록
    #     format = 'JPG', # 저장 포맷
    #     options = {'quality':90}, # 추가 옵션
    # )

    def __str__(self):
        return f'{self.id}번글 -{self.title}:{self.content}' 

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def str(self):
        return f'{self.article_id} {self.id}번 댓글 - {self.content}'
