from django.contrib import admin
from shopapp import models


@admin.register(models.ShopItemsModel)
class ShopItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'color', 'price']
