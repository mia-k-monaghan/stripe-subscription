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
