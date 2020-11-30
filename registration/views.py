from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView

from core.models import Subscription
from .forms import SignUpForm, LoginForm

import stripe
# Create your views here.

class SignupView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('registration:profile', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        stripe.api_key=settings.STRIPE_TEST_SECRET_KEY
        valid = super(SignupView, self).form_valid(form)
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        user = authenticate(email=email,
                            password=password)
        login(self.request, user)

        new_stripe_cust = stripe.Customer.create(
            email=email,
            name=form.cleaned_data.get('first_name') + " " + form.cleaned_data.get('last_name')
        )
        Subscription.objects.create(
            user=self.request.user,
            stripe_customer = new_stripe_cust.id
            )


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
