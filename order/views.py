from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Wishlist, Cart


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


def del_cart(request, pid):
    data = Cart.objects.get(id=pid)
    data.delete()
    return redirect("cart")
