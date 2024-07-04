from django.views import generic
from django.urls import reverse_lazy

from rest_framework.viewsets import ModelViewSet

from .models import Article, Comment
from .forms import AddCommentForm
from .serializers import ArticleSerializer
from .permissions import IsAdminOrReadOnly
from .services import *
from users.models import Profile


class HomeView(generic.ListView):
    model = Article
    template_name = 'forum/home.html'
    context_object_name = 'articles'


class WebDevView(generic.ListView):
    model = Article
    template_name = 'forum/webdev.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return filter_article('web')
        
    

class GameDevView(generic.ListView):
    model = Article
    template_name = 'forum/gamedev.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return filter_article('gamedev')
    

class AndroidView(generic.ListView):
    model = Article
    template_name = 'forum/android.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return filter_article('android')


class DataScienceView(generic.ListView):
    model = Article
    template_name = 'forum/data_science.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return filter_article('data_science')
    

class MachileLearningView(generic.ListView):
    model = Article
    template_name = 'forum/machine_learning.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return filter_article('ml')
    

class DevopsView(generic.ListView):
    model = Article
    template_name = 'forum/devops.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return filter_article('devops')
    

class CyberSecurityView(generic.ListView):
    model = Article
    template_name = 'forum/cyber_security.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return filter_article('cyber_security')
    

class TestingView(generic.ListView):
    model = Article
    template_name = 'forum/testing.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return filter_article('testing')
    

class AddArticleView(generic.CreateView):
    model = Article
    fields = ['title', 'text', 'image', 'category']
    template_name = 'forum/add_article.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    

class ArticleDetailView(generic.DetailView, generic.FormView):
    model = Article
    template_name = 'forum/article_detail.html'
    context_object_name = 'article'
    form_class = AddCommentForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = get_article(self.kwargs['pk'])
        context['comments'] = Comment.objects.filter(article=self.kwargs['pk']).select_related('author')

        return context
    
    def form_valid(self, form):
        form.instance.article = get_article(self.kwargs['pk'])
        form.instance.author = Profile.objects.get(user=self.request.user).select_related('user')
        form.save()
        return super().form_valid(form)
    

class ArticleUpdateView(generic.UpdateView):
    model = Article
    fields = ['title', 'text', 'image', 'category']
    template_name = 'forum/update_article.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    

class ArticleDeleteView(generic.DeleteView):
    model = Article
    success_url = reverse_lazy('profile')
    template_name = 'forum/delete_article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_article(self.kwargs['pk'])

        return context


class CommentUpdateView(generic.UpdateView):
    model = Comment
    template_name = 'forum/comment_update.html'
    fields = ['text']
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all().select_related('author')
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly, )