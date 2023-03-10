from django.contrib import admin
from authapp.models import AbstractUserModel

@admin.register(AbstractUserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_staff', 'is_superuser', 'border_color', 'profile_background', 'balance']
