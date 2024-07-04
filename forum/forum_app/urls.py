from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('api/users', views.ArticleViewSet)

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('web/', views.WebDevView.as_view(), name='webdev'),
    path('gamedev/', views.GameDevView.as_view(), name='gamedev'),
    path('android/', views.AndroidView.as_view(), name='android'),
    path('data_science/', views.DataScienceView.as_view(), name='data_science'),
    path('machine_learning/', views.MachileLearningView.as_view(), name='machine_learning'),
    path('devops/', views.DevopsView.as_view(), name='devops'),
    path('cyber_security/', views.CyberSecurityView.as_view(), name='cyber_security'),
    path('testing/', views.TestingView.as_view(), name='testing'),
    path('add-article/', views.AddArticleView.as_view(), name='add_article'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('articles/update/<int:pk>', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/<int:pk>', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('comment/update/<int:pk>', views.CommentUpdateView.as_view(), name='comment_update'),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)