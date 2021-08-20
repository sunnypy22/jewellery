from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from product.models import Category, Product
from order.models import Wishlist
from django.contrib import messages


# Create your views here.

def index(request):
    cat = Category.objects.all()
    pro = Product.objects.all().order_by('-id')[0:6]
    feature = Product.objects.all().filter(featured=True)

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

    return render(request, 'index.html', {'cat': cat, 'pro': pro, 'feature': feature})
