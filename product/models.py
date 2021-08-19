from django.db import models


# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=200, null=True, verbose_name="category")
    cat_img = models.FileField(null=True, verbose_name="Image")

    def __str__(self):
        return self.cat_name


class Jewellery_Type(models.Model):
    type_name = models.CharField(max_length=200, null=True, verbose_name="Jewellery Type")

    def __str__(self):
        return self.type_name


CHOICE_METAL = (
    ('Gold', 'Gold'),
)

CHOICE_METAL_COLOR = (
    ('yellow', 'yellow'),
)

CHOICE_GENDER = (
    ('Men', 'Men'),
    ('Women', 'Women'),
    ('Unisex', 'Unisex'),
)

CHOICE_OCCASION = (
    ('Work Wear', 'Work Wear'),
    ('Office Wear', 'Office Wear'),
)


class Product(models.Model):
    pro_cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="pro_cat",
                                verbose_name="Category")
    pro_jw_type = models.ForeignKey(Jewellery_Type, on_delete=models.CASCADE, null=True, related_name="pro_jw_type",
                                    verbose_name="Jewellery Type")
    pro_name = models.CharField(max_length=200, null=True, verbose_name="Product Name")
    gem_stone = models.CharField(max_length=200, null=True, verbose_name="Gem Stone")
    brand = models.CharField(max_length=200, null=True, verbose_name="Brand")
    metal = models.CharField(max_length=200, choices=CHOICE_METAL, default=CHOICE_METAL[0], verbose_name="Metal")
    height = models.CharField(max_length=200, null=True, verbose_name="Height")
    purity = models.CharField(max_length=200, null=True, verbose_name="Purity")
    gender = models.CharField(max_length=100, choices=CHOICE_GENDER, default=CHOICE_GENDER[0], verbose_name="Gender")
    occasion = models.CharField(max_length=200, choices=CHOICE_OCCASION, verbose_name="Occasion")
    width = models.CharField(max_length=200, null=True, verbose_name="Width")
    gross_weight = models.CharField(max_length=200, null=True, verbose_name="Gross Weight")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Price")
    offer = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Offer Price")
    featured = models.BooleanField(null=True, default=False, verbose_name="Featured")
    pro_img = models.FileField(verbose_name="Product Image")
    extra_desc = models.TextField(null=True, verbose_name="Description")

    def __str__(self):
        return self.pro_name

    @property
    def total(self):
        return self.price - self.offer


class Product_Color(models.Model):
    color_key = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    metal_color = models.CharField(max_length=50, verbose_name="Metal Color", choices=CHOICE_METAL_COLOR,
                                   default=CHOICE_METAL_COLOR[0])

    def __str__(self):
        return self.metal_color


class PostImage(models.Model):
    post = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')
