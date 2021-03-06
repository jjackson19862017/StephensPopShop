from django.shortcuts import render, redirect, reverse
from decimal import Decimal
from django.contrib import messages
from products.views import all_products
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

@login_required
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))
    price = request.POST.get('price')
    
    print("id: " + str(id))
    print("price: " + str(price))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity  
    else:
        cart[id] = cart.get(id, quantity)   

    request.session['cart'] = cart
    request.session['newprice'] = price
    messages.error(request, "Product added to cart.")
    return redirect(reverse('products'))

@login_required
def bid_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))
    price = request.POST.get('price')
    auction_num = int(request.POST.get('auction_num'))
    
    print("id: " + str(id))
    print("price: " + str(price))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity  
    else:
        cart[id] = cart.get(id, quantity) 

    
    request.session['cart'] = cart
    request.session['newprice'] = price
    request.session['auction_num'] = auction_num
    return redirect(reverse('bid_checkout'))

@login_required
def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))