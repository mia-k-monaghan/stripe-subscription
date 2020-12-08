// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/account/apikeys
let stripe = Stripe('pk_test_51HA03iLPfeVqJ0LGF7vJErtgow7hEF95tZc3jk1zhMmpXAcEfTR0mBSiPqu4oqlivxO9EAGfeIegQAIXzhUKbMWl00tdieedgt');
let elements = stripe.elements();
let card = elements.create('card', { style: style });

card.mount('#card-element');
card.on('change', function (event) {
  displayError(event);
});

function displayError(event) {
  changeLoadingStatePrices(false);
  let displayError = document.getElementById('card-element-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
}

var form = document.getElementById('subscription-form');
​
form.addEventListener('submit', function (ev) {
  ev.preventDefault();

function createPaymentMethod({ card }) {
  const customerId = {{ CUSTOMER_ID }};
  // Set up payment method for recurring usage
  let billingName = document.querySelector('#name').value;

  let priceId = document.getElementById('priceId').innerHTML.toUpperCase();
​
  stripe
    .createPaymentMethod({
      type: 'card',
      card: card,
      billing_details: {
        name: billingName,
      },
    })
    .then((result) => {
      if (result.error) {
        displayError(result);
      } else {
        createSubscription({
          customerId: customerId,
          paymentMethodId: result.paymentMethod.id,
          priceId: priceId,
        });
      }
    }
  }

  function createSubscription({ customerId, paymentMethodId, priceId }) {
  return (
    fetch('/create-subscription', {
      method: 'post',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify({
        customerId: customerId,
        paymentMethodId: paymentMethodId,
        priceId: priceId,
      }),
    })
      .then((response) => {
        return response.json();
      })
      // If the card is declined, display an error to the user.
      .then((result) => {
        if (result.error) {
          // The card had an error when trying to attach it to a customer.
          throw result;
        }
        return result;
      })
      // Normalize the result to contain the object returned by Stripe.
      // Add the additional details we need.
      .then((result) => {
        return {
          paymentMethodId: paymentMethodId,
          priceId: priceId,
          subscription: result,
        };
      })
      // Some payment methods require a customer to be on session
      // to complete the payment process. Check the status of the
      // payment intent to handle these actions.
      .then(handlePaymentThatRequiresCustomerAction)
      // If attaching this card to a Customer object succeeds,
      // but attempts to charge the customer fail, you
      // get a requires_payment_method error.
      .then(handleRequiresPaymentMethod)
      // No more actions required. Provision your service for the user.
      .then(onSubscriptionComplete)
      .catch((error) => {
        // An error has happened. Display the failure to the user here.
        // We utilize the HTML element we created.
        showCardError(error);
      })
  );
}
