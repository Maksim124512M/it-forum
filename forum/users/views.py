from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserSignupForm
from forum_app.models import Article
from .models import Profile


class UserSignupView(generic.FormView):
    form_class = UserSignupForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class ProfileView(LoginRequiredMixin, generic.ListView):
    model = Article
    template_name = 'users/profile.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)

        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)