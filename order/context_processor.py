from .models import Cart, Wishlist
from product.models import Category


def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(cart_user=request.user).count()
        return {'check_cart': cart}
    else:
        cart = 0
        return {'cart': cart}


def wishlist(request):
    if request.user.is_authenticated:
        data = Wishlist.objects.filter(wish_list_user=request.user).count()
        return {'check_wish': data}
    else:
        data = 0
        return {'check_wish': data}


def category(request):
    cat = Category.objects.all()
    return {'cat': cat}
