from django.shortcuts import get_object_or_404
from posts.models import Post

def cart_contents(request):
    """
    Ensures that cart contents are available when rendering every page
    """
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        post = get_object_or_404(Post, pk=id)
        total += quantity * post.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'post': post})
        
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
    