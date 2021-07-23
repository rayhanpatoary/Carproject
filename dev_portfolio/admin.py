from django.contrib import admin
from .models import Developer


# DeveloperAdmin
@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number']
