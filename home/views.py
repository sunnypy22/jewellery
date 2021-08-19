from django.shortcuts import render, redirect
from product.models import Category, Product

# Create your views here.

def index(request):
    cat = Category.objects.all()
    pro = Product.objects.all().order_by('-id')[0:6]
    feature = Product.objects.all().filter(featured=True)
    return render(request, 'index.html',{'cat':cat,'pro':pro,'feature':feature})
