from django.contrib import admin
from .models import Product, Category, emp


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price', 'quantity', 'confirm']
    list_filter = ['price']


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name']


class EmpAdmin(admin.ModelAdmin):
    model = emp
    list_display = ['username', 'email']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(emp, EmpAdmin)
