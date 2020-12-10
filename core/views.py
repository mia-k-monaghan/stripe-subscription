from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

import json
import stripe

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

# Create your views here.
class CheckoutView(LoginRequiredMixin,View):
    def get(self, *args,**kwargs):
        return render(self.request, 'core/subscribe.html')


@csrf_exempt
@login_required
def createSubscription(request):
    if request.method=="POST":
        data = json.loads(request.body)
        try:
            # Attach the payment method to the customer
            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                customer=request.user.stripe_customer,
            )
            # Set the default payment method on the customer
            stripe.Customer.modify(
                request.user.stripe_customer,
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            # Create the subscription
            subscription = stripe.Subscription.create(
                customer=request.user.stripe_customer,
                items=[
                    {
                        'price': data['priceId']
                    }
                ],
                expand=['latest_invoice.payment_intent'],
            )
            return JsonResponse(subscription)
        except Exception as e:
            print(str(e))
            return JsonResponse({'message': str(e)}, status=200)
