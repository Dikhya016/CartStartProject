from django.contrib import admin
from .models import (
    User, Company, Customer, Seller, Category, Product, Order, OrderItem, Address, Review, Cart, CartItem, Wishlist,
    WishlistItem, Payment, Coupon, ShippingMethod
)

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(ShippingMethod)
