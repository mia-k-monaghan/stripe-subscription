from django.urls import path
from .views import SignupView, LoginView,ProfileView
from django.contrib.auth import views as auth_views

app_name = 'registration'

urlpatterns = [
    path('', SignupView.as_view(), name='index'),
    path('profile/<pk>',ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
