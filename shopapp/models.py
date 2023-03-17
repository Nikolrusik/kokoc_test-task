from django.db import models
from authapp.models import AbstractUserModel

ITEM_TYPES = (
    ("BORDER", "Border color"),
    ("BACKGROUND", "Profile background")
)


class ShopItemsModel(models.Model):
    name = models.CharField(verbose_name="Name color", max_length=255)
    type = models.CharField(verbose_name="Type item",
                            choices=ITEM_TYPES, default="BORDER", max_length=100)
    color = models.CharField(verbose_name="Color", max_length=100)
    price = models.FloatField(verbose_name="Item price", default=0.0)

    class Meta:
        verbose_name = "Shop item"
        verbose_name_plural = "Shop items"


class UserItemsModel(models.Model):
    item = models.ForeignKey(
        ShopItemsModel, on_delete=models.SET_NULL, null=True, verbose_name="Shop item")
    user = models.ForeignKey(AbstractUserModel, on_delete=models.CASCADE, verbose_name="User")
    type = models.CharField(verbose_name="Type item",
                            choices=ITEM_TYPES, default="BORDER", max_length=100)
    color = models.CharField(verbose_name="Color", max_length=100)

    class Meta:
        verbose_name = "User item"
        verbose_name = "User items"