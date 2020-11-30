from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    stripe_customer = models.CharField(max_length=100,
        help_text = "The user's Stripe Customer object, if it exists")
    stripe_subscription = models.CharField(max_length=100,
        help_text = "The user's Stripe Customer object, if it exists")

    def __str__(self):
        return (self.email)
