from django.shortcuts import render
from shop.models import Product,Store
# Create your views here.
def list_product_view(request):
    prod = Product.objects.all()
    context = {
        "pro":prod
    }
    return render(request,"shop/listprod.html",context)