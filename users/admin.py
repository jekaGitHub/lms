from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "password", "phone", "city",)
    list_filter = ("email", "city")
    search_fields = ("email", "phone")
