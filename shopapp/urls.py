from django.urls import path
from shopapp import views
from shopapp.apps import ShopappConfig

app_name = ShopappConfig.name

urlpatterns = [
    path("items/", views.Items.as_view(), name="items"),
    path("user_items/", views.UserItems.as_view(), name="user_items"),
]