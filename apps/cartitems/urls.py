from django.urls import path

from apps.cartitems.views import cart_view, add_cart, plus_quantity_cart, minus_quantity_cart, remove_cart_item


urlpatterns = [
    path('cart/', cart_view, name='cart_view'),
    path('add_cart_item/<int:pk>/', add_cart, name='add_cart_package'),
    path('add-quantity/<int:pk>/', plus_quantity_cart, name='plus_quantity'),
    path('rem-quantity/<int:pk>/', minus_quantity_cart, name='minus_quantity'),
    path('remove-cart-item/<int:pk>/', remove_cart_item, name='remove_cart_item'),
]