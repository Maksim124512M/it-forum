from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile
from django.utils.timezone import now

CATEGORIES = [
    ('all', 'All'),
    ('web', 'WEB Development'),
    ('gamedev', 'Gamedev'),
    ('mobile', 'Mobile Development'),
    ('data_science', 'Data Science'),
    ('ml', 'Machine Learning'),
    ('devops', 'DevOps'),
    ('cyber_security', 'Cyber security'),
    ('testing', 'Testing'),
]

class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='article-default-image.png')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, choices=CATEGORIES, default='all')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk':self.id})
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return f'Comment for lesson "{self.article.title}"'
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk':self.article.id})
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
