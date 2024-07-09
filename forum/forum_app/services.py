from .models import Article


def filter_article(category):
    return Article.objects.filter(category=category).order_by('-date').select_related('author')


def get_article(article):
    return Article.objects.get(id=article)