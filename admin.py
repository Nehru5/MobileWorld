from django.contrib import admin
from shopping.models import UserProfile, UserDetails, Product, Order, Cart

admin.site.register(UserProfile)
admin.site.register(UserDetails)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)

