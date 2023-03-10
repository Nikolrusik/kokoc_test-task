from django.contrib import admin
from authapp import models


@admin.register(models.AbstractUserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
