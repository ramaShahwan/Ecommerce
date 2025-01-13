from django.contrib import admin
from .models import *

# Customizing the Bonus Admin
class BonusAdmin(admin.ModelAdmin):
    list_display = ('customer', 'amount')
    search_fields = ('customer__user__first_name', 'customer__user__last_name')
    ordering = ('customer',)

# Customizing the Complaint Admin
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'subject', 'created_at')
    search_fields = ('user_email', 'subject')
    ordering = ('created_at',)

# Customizing the Address Admin
class AddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'street', 'city', 'description', 'postal_code')
    search_fields = ('customer__user__first_name', 'customer__user__last_name', 'city', 'description')
    ordering = ('customer', 'city')

# Customizing the Brand Admin
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

# Customizing the Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

# Customizing the Discount Admin
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('value', 'start_date', 'end_date', 'status')
    list_filter = ('status',)
    search_fields = ('value',)
    ordering = ('start_date',)

# Customizing the Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity_available', 'id_brand', 'id_category')
    search_fields = ('name', 'id_brand__name', 'id_category__name')
    list_filter = ('id_brand', 'id_category', 'release_date')
    ordering = ('name',)

# Customizing the CreditCard Admin
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('cardholder_name', 'card_number', 'expiration_date', 'customer', 'balance')
    search_fields = ('cardholder_name', 'card_number', 'customer__user__first_name', 'customer__user__last_name')
    ordering = ('customer',)

# Customizing the ShoppingCart Admin
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('customer', 'created_at')
    search_fields = ('customer__user__first_name', 'customer__user__last_name')
    ordering = ('created_at',)

# Customizing the ShoppingCart_Items Admin
class ShoppingCartItemsAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'price')
    search_fields = ('cart__customer__user__first_name', 'cart__customer__user__last_name', 'product__name')
    ordering = ('cart',)

# Customizing the Order Admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id_cart_product', 'order_date', 'total_amount', 'payment_status', 'status')
    search_fields = ('id_cart_product__cart__customer__user__first_name', 'id_cart_product__cart__customer__user__last_name', 'id_cart_product__product__name')
    list_filter = ('payment_status', 'status', 'order_date')
    ordering = ('order_date',)

# Registering the models with their respective custom admins
admin.site.register(Bonus, BonusAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CreditCard, CreditCardAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(ShoppingCart_Items, ShoppingCartItemsAdmin)
admin.site.register(Order, OrderAdmin)