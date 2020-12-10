from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('create-subscription', views.createSubscription, name='create-subscription'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),

]
