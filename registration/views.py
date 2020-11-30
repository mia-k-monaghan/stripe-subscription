from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView

from core.models import Subscription
from .forms import SignUpForm, LoginForm
# Create your views here.

class SignupView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('registration:profile', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        valid = super(SignupView, self).form_valid(form)
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        user = authenticate(email=email,
                            password=password)
        login(self.request, user)

        Subscription.objects.create(user=self.request.user)

        return valid

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('registration:profile', kwargs={'pk': self.request.user.pk})

class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    context_object_name = 'user'
    template_name = 'registration/profile.html'
