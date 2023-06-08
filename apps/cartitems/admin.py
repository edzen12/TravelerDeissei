from django.contrib import admin

from apps.cartitems.models import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user']
