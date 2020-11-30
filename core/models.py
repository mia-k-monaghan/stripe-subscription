from django.db import models
from django.conf import settings
# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    stripe_customer = models.CharField(max_length=100,blank=True,
        help_text = "The user's Stripe Customer object, if it exists")
    stripe_subscription = models.CharField(max_length=100,blank=True,
        help_text = "The user's Stripe Customer object, if it exists")

    def __str__(self):
        return str(self.user)
