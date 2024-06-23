from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from .models import Article, Comment
from .forms import AddCommentForm
from users.models import Profile
from django.urls import reverse_lazy


class HomeView(generic.ListView):
    model = Article
    template_name = 'forum/home.html'
    context_object_name = 'articles'


class WebDevView(generic.ListView):
    model = Article
    template_name = 'forum/webdev.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return self.model.objects.filter(category='web')
    

class GameDevView(generic.ListView):
    model = Article
    template_name = 'forum/gamedev.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return self.model.objects.filter(category='gamedev')
    

class AndroidView(generic.ListView):
    model = Article
    template_name = 'forum/android.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return self.model.objects.filter(category='android')


class DataScienceView(generic.ListView):
    model = Article
    template_name = 'forum/data_science.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return self.model.objects.filter(category='data_science')
    

class MachileLearningView(generic.ListView):
    model = Article
    template_name = 'forum/machine_learning.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return self.model.objects.filter(category='ml')
    

class DevopsView(generic.ListView):
    model = Article
    template_name = 'forum/devops.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return self.model.objects.filter(category='devops')
    

class CyberSecurityView(generic.ListView):
    model = Article
    template_name = 'forum/cyber_security.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return self.model.objects.filter(category='cyber_security')
    

class TestingView(generic.ListView):
    model = Article
    template_name = 'forum/testing.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return self.model.objects.filter(category='testing')
    

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
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['title'] = Article.objects.get(id=self.kwargs['pk'])
        context['comments'] = Comment.objects.filter(article=self.kwargs['pk'])

        return context
    
    def form_valid(self, form):
        form.instance.article = Article.objects.get(id=self.kwargs['pk'])
        form.instance.author = Profile.objects.get(user=self.request.user)
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
        context = super(ArticleDeleteView, self).get_context_data(**kwargs)
        context['article'] = Article.objects.get(id=self.kwargs['pk'])

        return context


class CommentUpdateView(generic.UpdateView):
    model = Comment
    template_name = 'forum/comment_update.html'
    fields = ['text']
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
