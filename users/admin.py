from django.contrib import admin

from users.models import User

@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
   list_display = ("email",)
   fields = ("email",)
   readonly_fields = ("email",)
   search_fields = ("email",)


