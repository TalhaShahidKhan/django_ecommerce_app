from django.urls import path
from shop.views import list_product_view,create_product_view,create_store_view
urlpatterns = [
    path('',list_product_view,name="pro_list"),
    path('add/',create_product_view,name="add_pro"),
    path('adds/',create_store_view,name="add_store"),
]

app_name = "shop"