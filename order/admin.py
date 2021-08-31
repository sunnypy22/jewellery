from django.contrib import admin
from .models import Wishlist, Cart, Checkout, Order_History
# Register your models here.

class Extra_Wish(admin.ModelAdmin):
    list_filter = ['wish_list_user','wish_list_product']
    list_display = ['wish_list_user','wish_list_product']
    readonly_fields = ['wish_list_user','wish_list_product','wish_list_status']

admin.site.register(Wishlist,Extra_Wish)
admin.site.register(Cart)
admin.site.register(Checkout)
admin.site.register(Order_History)