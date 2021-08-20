from django.contrib import admin
from .models import User
# Register your models here.


class Extra_User(admin.ModelAdmin):
    list_display = ['username','email','last_login']
    list_filter = ['username','email']
    readonly_fields = ['password','last_login','date_joined']

admin.site.register(User, Extra_User)