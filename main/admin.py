from django.contrib import admin
from .models import Product,Category,Order,OrderProduct,CustomUser,Review

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Category)
admin.site.register(CustomUser)
admin.site.register(Review)