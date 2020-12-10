# Stripe Subscription
A Django project demonstrating how to create a simple subscription service website with Stripe.

This project walks the user through a simple website subscription sign up process using Django and Stripe. It contains the following elements:

1. Contains a custom Django user model, requiring the user to only provide email  & password for authentication (instead of username)
2. Automatically logs the user in after sign up
3. Creates a Stripe Subscription & Stripe Customer for the user upon successful signup & payment
4. Collects payment information from the user
5. Securely stores payment information in Stripe
6. Retrieves user subscription & payment details and displays them to user in a User Profile
7. Connects the user's profile to a Stripe Billing Session, allowing the user to manage Payment Methods and other subscription detatils
8. Manages Users and Subscriptions with local Django Models
