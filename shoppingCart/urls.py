from django.urls import path
from . import views

app_name = "shoppingCars"

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<int:item_id>', views.add_item_to_cart, name="add_item"),
    path('remove/<int:item_id>', views.remove_item_in_cart, name="remove_item"),
]
