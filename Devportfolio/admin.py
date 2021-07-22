from django.contrib import admin
from.models import Developer


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['first_name' , 'last_name', 'email', 'phone_number']


