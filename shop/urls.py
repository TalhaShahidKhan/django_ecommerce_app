from django.urls import path
from shop.views import list_product_view,product_details_view,create_product_view,update_product_view,delt_product
urlpatterns = [
    path('',list_product_view,name="pro_list"),
    path('pro/add/',create_product_view,name="pro_add"),
    path('pro/<str:slug>/',product_details_view,name="pro_det"),
    path('pro/upd/<str:slug>/',update_product_view,name="pro_upd"),
    path('pro/dlt/<str:slug>/',delt_product,name="pro_dlt"),
]

app_name = "shop"