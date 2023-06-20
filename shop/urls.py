from django.urls import path
from shop.views import list_product_view,product_details_view,create_product_view,update_product_view,seller
urlpatterns = [
    path('',list_product_view,name="pro_list"),
    path('pro/sell/',seller,name="pro_sell"),
    path('pro/add/',create_product_view,name="pro_add"),
    path('pro/<str:slug>/',product_details_view,name="pro_det"),
    path('pro/upd/<str:slug>/',update_product_view,name="pro_upd"),
    path('pro/dlt/<str:slug>/',update_product_view,name="pro_upd"),
]

app_name = "shop"