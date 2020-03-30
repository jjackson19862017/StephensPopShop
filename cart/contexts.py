from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal

def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})
    price = request.session.get('newprice', {})
    auction_num = request.session.get('auction_num', {})
    price = Decimal(price)
    price = round(price, 2)
    print("AN: "+str(auction_num))
    print("Price: " + str(price))
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        if price > 0.00:
            
            total += quantity * price
            print("A: "+ str(total))
        else:
            total += quantity * product.instant_buy_price
            print("B: "+ str(total))
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
        print("product: "+str(product))
        print("total: "+str(total))
        print("product count: "+str(product_count))
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count, 'price': price, 'auction_num':auction_num}