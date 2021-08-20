from django.db.models import Count
from django.shortcuts import render, redirect
from .models import Product, CHOICE_METAL_COLOR, CHOICE_GENDER, CHOICE_OCCASION, CHOICE_METAL, Category, Product_Color,PostImage
from order.models import Wishlist, Cart
from django.contrib import messages
# Create your views here.

def products(request, pid):
    category = Category.objects.get(id=pid)
    pro = Product.objects.all().filter(pro_cat_id=pid)
    color = CHOICE_METAL_COLOR[0:]
    gender = CHOICE_GENDER[0:]
    occasion = CHOICE_OCCASION[0:]
    metal = CHOICE_METAL[0:]
    cat = Category.objects.all()
    key_a = request.GET.get('order_by')
    if key_a == "High-To-Low":
        order_by_price_h_to_l = Product.objects.all().filter(pro_cat_id=pid).order_by('-price')
        return render(request, 'collection-left.html',
                  {'category': category, 'pro': order_by_price_h_to_l, 'color': color, 'gender': gender, 'occasion': occasion,
                   'metal': metal, 'cat': cat})
    elif key_a == "Low-To-High":
        order_by_price_l_to_h = Product.objects.all().filter(pro_cat_id=pid).order_by('price')
        return render(request, 'collection-left.html',
                  {'category': category, 'pro': order_by_price_l_to_h, 'color': color, 'gender': gender, 'occasion': occasion,
                   'metal': metal, 'cat': cat})
    elif key_a == "A-Z":
        A_Z = Product.objects.all().filter(pro_cat_id=pid).order_by('pro_name')
        return render(request, 'collection-left.html',
                      {'category': category, 'pro': A_Z, 'color': color, 'gender': gender,
                       'occasion': occasion,
                       'metal': metal, 'cat': cat})
    elif key_a == "Z-A":
        Z_A = Product.objects.all().filter(pro_cat_id=pid).order_by('-pro_name')
        return render(request, 'collection-left.html',
                      {'category': category, 'pro': Z_A, 'color': color, 'gender': gender,
                       'occasion': occasion,
                       'metal': metal, 'cat': cat})
    elif key_a == "Oldest_to_Newest":
        Oldest_to_Newest = Product.objects.all().filter(pro_cat_id=pid).order_by('id')
        return render(request, 'collection-left.html',
                      {'category': category, 'pro': Oldest_to_Newest, 'color': color, 'gender': gender,
                       'occasion': occasion,
                       'metal': metal, 'cat': cat})
    elif key_a == "Newest_to_Oldest":
        Newest_to_Oldest = Product.objects.all().filter(pro_cat_id=pid).order_by('-id')
        return render(request, 'collection-left.html',
                      {'category': category, 'pro': Newest_to_Oldest, 'color': color, 'gender': gender,
                       'occasion': occasion,
                       'metal': metal, 'cat': cat})
    else:
        pass
    if request.method == "POST":
        if request.user.is_authenticated:
            if "wishlist_form" in request.POST:
                pro_id = request.POST.get('pro_id')
                pro_name = request.POST.get('pro_name')
                if Wishlist.objects.filter(wish_list_user = request.user,wish_list_product=pro_id).exists():
                    messages.warning(request, 'Product {} already exists in wishlist!'.format(pro_name))
                else:
                    if request.user.is_authenticated:
                        data = Wishlist.objects.create(wish_list_product_id=pro_id, wish_list_user=request.user,
                                                   wish_list_status=True)

                        data.save()
                        return redirect("wishlist")
                    else:
                        return redirect("signin")
        else:
            return redirect("signin")
    else:
        pass
    return render(request, 'collection-left.html',
                  {'category': category, 'pro': pro, 'color': color, 'gender': gender, 'occasion': occasion,
                   'metal': metal, 'cat': cat})


def product_view(request, pid):
    pro = Product.objects.get(id=pid)
    color = Product_Color.objects.filter(color_key_id=pid)
    image = PostImage.objects.filter(post_id=pid)
    if request.method == "POST":
        if request.user.is_authenticated:
            if "wishlist_form" in request.POST:
                pro_id = request.POST.get('pro_id')
                pro_name = request.POST.get('pro_name')
                if Wishlist.objects.filter(wish_list_user = request.user,wish_list_product=pro_id).exists():
                    messages.warning(request, 'Product {} already exists in wishlist!'.format(pro_name))
                else:
                    if request.user.is_authenticated:
                        data = Wishlist.objects.create(wish_list_product_id=pro_id, wish_list_user=request.user,
                                                   wish_list_status=True)

                        data.save()
                        return redirect("wishlist")
                    else:
                        return redirect("signin")
            elif "cart_form" in request.POST:
                product_color = request.POST.get('cart_color_item')
                check_cart = Cart.objects.filter(cart_user=request.user, cart_product_id=pro.id, cart_color=product_color)
                if check_cart:
                    data = Cart.objects.get(cart_user=request.user, cart_product_id=pro.id,cart_color=product_color)
                    data.cart_quantity += int(request.POST.get("quantity"))
                    data.cart_color = product_color
                    data.save()
                    return redirect("cart")
                else:
                    quantity = int(request.POST.get("quantity"))
                    if product_color == "":
                        messages.error(request, 'Please Choose Your Colour for Better Experience')
                    else:
                        data = Cart(cart_user=request.user, cart_product_id=pro.id, cart_status=True,cart_color=product_color,
                                cart_quantity=quantity)
                        data.save()
                        return redirect("cart")
        else:
            return redirect("signin")
    else:
        pass
    return render(request, 'product.html', {'pro': pro,'color':color,'image':image})
