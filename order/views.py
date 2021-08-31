from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Wishlist, Cart, Checkout, Order_History
from django.contrib import messages
from product.models import Product_Color, PostImage
import razorpay
from django.views.decorators.csrf import csrf_exempt

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
            Cart.objects.filter(cart_user=request.user).update(cart_quantity=quantity, cart_color=cart_color_item)
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


def checkout(request):
    data = Cart.objects.filter(cart_user=request.user.id)

    if request.method == 'POST':
        ammount = float(request.POST.get("subtotal_cart")) * 100
        main_price = float(request.POST.get("subtotal_cart"))
        product = request.POST.getlist("product[]")
        ord_color = request.POST.getlist("ord_color[]")
        ord_quantity = request.POST.getlist("ord_quantity[]")
        billing_postcode = request.POST.get("billing_postcode")
        order_address = request.POST.get("order_address")
        billing_phone = request.POST.get("billing_phone")
        client = razorpay.Client(auth=("rzp_test_l5VpO7rP3PiD3H", "brki2hlaIjeRC78vVdkm0izV"))
        payment = client.order.create({'amount': ammount, 'currency': 'INR', 'payment_capture': '1'})
        coffee = Checkout(name=request.user, product=product, ammount=main_price, payment_id=payment['id'],
                          billing_postcode=billing_postcode, order_address=order_address, billing_phone=billing_phone,
                          order_status="Prepare To Dispatch")
        coffee.save()

        ord_payment_id = coffee.payment_id
        for product, ord_quantity,ord_color in zip(product, ord_color, ord_quantity):
            data = Order_History.objects.create(ord_product=product, ord_color=ord_color,
                                                ord_quantity=ord_quantity, history_user_name=request.user,
                                                ord_payment_id=ord_payment_id, order_checkout_id=coffee.id)
            data.save()
        details = Cart.objects.filter(cart_user=request.user.id)

        return render(request, 'checkout.html', {'payment': payment, 'details': details})
    return render(request, 'checkout.html', {'data': data})


@csrf_exempt
def success(request):
    if request.method == 'POST':
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        user = Checkout.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()

        try:
            if user.paid == True:
                user = str(request.user.id)

                cart = Cart.objects.raw(
                    'DELETE FROM order_cart WHERE cart_user_id="' + user + '"')
                return render(request, 'success.html', {'cart': cart})
        except TypeError:
            return render(request, 'success.html')
        return render(request, 'success.html')