from django.contrib import admin

from shop.models import Product



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'color', 'price', 'category', 'description', 'created_at')
    fields = ('title', 'image', 'color', 'price', 'category', 'description', 'created_at')
    readonly_fields = ('created_at',)
    search_fields = ('title', 'price', 'category')

    def save_form(self, request, form, change):
        return super().save_form(request, form, change)

