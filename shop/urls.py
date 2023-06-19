from django.urls import path
from shop.views import list_product_view
urlpatterns = [
    path('',list_product_view,name="pro_list"),
]

app_name = "shop"