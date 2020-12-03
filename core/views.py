from django.shortcuts import render
from django.conf import settings

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

# Create your views here.
