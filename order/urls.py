from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.wishlist, name="wishlist"),
    path('del_wishlist/<int:pid>', views.del_wishlist, name="del_wishlist"),

]
