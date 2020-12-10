// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/account/apikeys
let stripe = Stripe('pk_test_51HA03iLPfeVqJ0LGF7vJErtgow7hEF95tZc3jk1zhMmpXAcEfTR0mBSiPqu4oqlivxO9EAGfeIegQAIXzhUKbMWl00tdieedgt');
let elements = stripe.elements();
let style = {
  base: {
    color: "#32325d",
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4"
    }
  },
  invalid: {
    color: "#fa755a",
    iconColor: "#fa755a"
  }
};
let card = elements.create('card', { style: style });

card.mount('#card-element');
card.on('change', function(event) {
  displayError(event);
});

var form = document.getElementById('subscription-form');
form.addEventListener('submit', function (ev) {
  ev.preventDefault();
  createPaymentMethod({ card });
  });



function createPaymentMethod({ card }) {
  // Set up payment method for recurring usage
  let billingName = document.querySelector('#name').value;
  console.log(billingName);
  stripe.createPaymentMethod({
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
        const paymentParams = {
          paymentMethodId: result.paymentMethod.id,
          last4: result.paymentMethod.card.last4,
          priceId: document.getElementById("priceId").innerHTML,
        };
        createSubscription(paymentParams);
      }
    });
  }

function createSubscription({ paymentMethodId, last4, priceId }) {

    return (
      fetch('/create-subscription', {
       method: 'POST',
       headers: {
         'Content-type': 'application/json',
         'X-CSRFToken':'{{ csrf_token }}',
       },
       credentials: 'same-origin',
       body: JSON.stringify({
          paymentMethodId: paymentMethodId,
          last4: last4,
          priceId: priceId,
        }),
     })
     .then((response) => {
       return response.json();
     })
     // If the card is declined, display an error to the user.
     .then((result) => {
       if (result.error) {
         console.log("The card had an error when trying to attach it to a customer.");
         // The card had an error when trying to attach it to a customer.
         throw result;
       }
       return result;
     })
     .then((result) => {

          window.location.href = '/success';

      })
     .catch((error) => {
       // An error has happened. Display the failure to the user here.
       // We utilize the HTML element we created.
       // showCardError(error);
       displayError(error)
       return console.log(error+" " + paymentMethodId +" "+ priceId);
     })
)}

function displayError(event) {
  // changeLoadingStatePrices(false);
  let displayError = document.getElementById('card-element-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
}
