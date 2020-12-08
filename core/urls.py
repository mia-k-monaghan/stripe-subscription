from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('create-subscription', views.createSubscription, name='subscribe'),

]
