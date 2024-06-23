from django.views import generic
from .forms import UserSignupForm, ProfileImageForm
from forum_app.models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile


class UserSignupView(generic.FormView):
    form_class = UserSignupForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class ProfileView(LoginRequiredMixin, generic.FormView):
    form_class = ProfileImageForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(author=self.request.user)
        context['profile'] = Profile.objects.get(user=self.request.user)

        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save(commit=False)
        return super().form_valid(form)