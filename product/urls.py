from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:pid>', views.products, name="products"),
    path('product_view/<int:pid>', views.product_view, name="product_view"),
]
