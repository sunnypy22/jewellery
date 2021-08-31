from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.wishlist, name="wishlist"),
    path('del_wishlist/<int:pid>', views.del_wishlist, name="del_wishlist"),
    path('cart/', views.cart, name="cart"),
    path('update_cart/<int:pid>', views.update_cart, name="update_cart"),
    path('del_cart/<int:pid>', views.del_cart, name="del_cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('success/', views.success, name="success"),

]
