from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseRedirect 
import random
from django.shortcuts import render
from shop.models import Product
from purchase.models import Purchase
# Create your views here.


def purchase_start_view(request):
    if not request.method == "POST":
        return HttpResponseBadRequest()
    if not request.user.is_authenticated:
        return HttpResponseBadRequest()
    slug = request.POST.get("slug")
    obj = Product.objects.get(slug = slug)
    purchase = Purchase.objects.create(user = request.user ,product = obj)
    request.session["purchase_id"] = purchase.id
    return render(request,'purchase/')

def purchase_success_view(request):
    purchase_id = request.session.get("purchase_id")
    purchase = Purchase.objects.get(id = purchase_id)
    purchase.completed = True
    purchase.save()
    return HttpResponse(f"Successfull {purchase_id}")

def purchase_stopped_view(request):
    return HttpResponse("Stopped")