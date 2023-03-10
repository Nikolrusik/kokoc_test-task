from django.db import models
from authapp.models import AbstractUserModel

ITEM_TYPES = (
    ("BORDER", "Border color"),
    ("BACKGROUND", "Profile background")
)
class ShopItemsModel(models.Model):
    name = models.CharField(verbose_name="Name color", max_length=255)
    type = models.CharField(verbose_name="Type item", choices=ITEM_TYPES, default="BORDER", max_length=100)
    color = models.CharField(verbose_name="Color", max_length=100)
    price = models.FloatField(verbose_name="Item price", default=0.0)

class UserItemsModel(models.Model):
    item = models.ForeignKey(ShopItemsModel, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(AbstractUserModel, on_delete=models.CASCADE)
    type = models.CharField(verbose_name="Type item", choices=ITEM_TYPES, default="BORDER", max_length=100)
    color = models.CharField(verbose_name="Color", max_length=100)