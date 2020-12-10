from django.db import models
from django.conf import settings
# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscriptions")
    active = models.BooleanField(default=False)
    stripe_subscription = models.CharField(max_length=100,blank=True,
        help_text = "The user's Stripe Customer object, if it exists")
    last4 = models.CharField(max_length=4,blank=True,
        help_text = "The user's last 4 credit card digits, if they exist")

    def __str__(self):
        return str(self.user)
