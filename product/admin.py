from django.contrib import admin
from .models import Category, Jewellery_Type, Product, Product_Color, PostImage
# Register your models here.


class PostImageAdmin(admin.TabularInline):
    model = PostImage
    extra = 0

class ProColor(admin.TabularInline):
    model = Product_Color
    extra = 0

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin,ProColor]


admin.site.register(Category)
admin.site.register(Jewellery_Type)
