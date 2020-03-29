from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})
    price = request.session.get('newprice', {})
    print("newbie: "+ str(price))
    cart_items = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        
        total += quantity * price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
        print("product: "+str(product))
        print("total: "+str(total))
        print("product count: "+str(product_count))
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count, 'price': price}