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
  var displayError = document.getElementById('card-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
});

var form = document.getElementById('subscription-form');
form.addEventListener('submit', function (ev) {
  ev.preventDefault();
  createPaymentMethod({ card });
  });


function displayError(event) {
  // changeLoadingStatePrices(false);
  let displayError = document.getElementById('card-element-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
}

function createPaymentMethod({ card }) {
  // Set up payment method for recurring usage
  let billingName = document.querySelector('#name').value;
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
           priceId: document.getElementById("priceId").innerHTML,
           paymentMethodId: result.paymentMethod.id,
       };
       fetch('/create-subscription', {
        method: 'post',
        headers: {
          'Content-type': 'application/json',
          'X-CSRFToken':'{{ csrf_token }}',
        },
        credentials: 'same-origin',
        body: JSON.stringify(paymentParams),
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
        .catch((error) => {
          // An error has happened. Display the failure to the user here.
          // We utilize the HTML element we created.
          // showCardError(error);
          console.log(error);
        })

      }
    });
  }
