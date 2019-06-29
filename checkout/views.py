from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from posts.models import Post, Voter
import stripe

stripe_api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get("cart", {})
            total = 0
            for id, quantity in cart.items():
                post = get_object_or_404(Post, pk=id)
                total += quantity * post.price
                order_line_item = OrderLineItem(
                    order = order,
                    post = post,
                    quantity = quantity
                    )
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                    )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid!")
                request.session['cart'] = {}
                
                # increment upvotes by "quantity".
                post = get_object_or_404(Post, pk=id)
                post.upvotes += quantity
                post.save()
                Voter.objects.create(id=id, user_id=request.user.id)
                
                return redirect(reverse('get_posts'))
            else:
                messages.error(request, "Unable to make payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout.html", {'order_form':order_form, 'payment_form':payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})