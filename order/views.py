from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Wishlist, Cart
from django.contrib import messages
from product.models import Product_Color, PostImage


# Create your views here.
@login_required
def wishlist(request):
    data = Wishlist.objects.filter(wish_list_user=request.user)
    return render(request, 'wishlist.html', {'data': data})


def del_wishlist(request, pid):
    data = Wishlist.objects.get(id=pid)
    data.delete()
    return redirect("wishlist")


@login_required
def cart(request):
    data = Cart.objects.filter(cart_user=request.user)
    return render(request, 'cart.html', {'data': data})


def update_cart(request, pid):
    try:
        data = Cart.objects.get(id=pid, cart_user=request.user)
        pro_id = data.cart_product.id
        color = Product_Color.objects.filter(color_key_id=pro_id)
        image = PostImage.objects.filter(post_id=pro_id)
        if request.method == "POST":
            quantity = request.POST.get('quantity')
            cart_color_item = request.POST.get('cart_color_item')
            Cart.objects.filter(cart_user = request.user).update(cart_quantity = quantity,cart_color = cart_color_item)
            return redirect("cart")
        else:
            pass
        return render(request, 'update_cart.html', {'pro': data, 'color': color, 'image': image})
    except:
        messages.error(request, 'You are unauthorized to access the link')
        return redirect("cart")


def del_cart(request, pid):
    data = Cart.objects.get(id=pid)
    data.delete()
    return redirect("cart")
