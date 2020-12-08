from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import json
import stripe

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

# Create your views here.
def createSubscription(request):
    if request.method=='POST':
        data = json.loads(request.data)
        try:
            # Attach the payment method to the customer
            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                customer=data['customerId'],
            )
            # Set the default payment method on the customer
            stripe.Customer.modify(
                data['customerId'],
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            # Create the subscription
            subscription = stripe.Subscription.create(
                customer=data['customerId'],
                items=[
                    {
                        'price': 'price_HGd7M3DV3IMXkC'
                    }
                ],
                expand=['latest_invoice.payment_intent'],
            )
            return JsonResponse(subscription)
        except Exception as e:
            return JsonResponse(error={'message': str(e)}), 200

    else:
        return render(request, 'core/subscribe.html')
