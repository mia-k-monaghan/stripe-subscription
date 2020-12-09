from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import json
import stripe

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

# Create your views here.
@login_required
@csrf_exempt
def createSubscription(request):
    if request.method=='POST':
        data = json.loads(request.data)
        try:
            # Attach the payment method to the customer
            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                customer=request.user.kwargs['stripe_customer'],
            )
            # Set the default payment method on the customer
            stripe.Customer.modify(
                request.user.kwargs['stripe_customer'],
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            # Create the subscription
            subscription = stripe.Subscription.create(
                customer=request.user.kwargs['stripe_customer'],
                items=[
                    {
                        'price': data['priceId']
                    }
                ],
                expand=['latest_invoice.payment_intent'],
            )
            return JsonResponse(subscription)
        except Exception as e:
            return JsonResponse(error={'message': str(e)}), 200

    else:
        return render(request, 'core/subscribe.html')
