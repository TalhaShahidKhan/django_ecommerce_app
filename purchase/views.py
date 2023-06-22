from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseRedirect 
import random
from django.shortcuts import render
from shop.models import Product
from purchase.models import Purchase
# Create your views here.


def purchase_start_view(requset):
    if not requset.method == "POST":
        return HttpResponseBadRequest()
    if not requset.user.is_authenticated:
        return HttpResponseBadRequest()
    slug = requset.POST.get("slug")
    obj = Product.objects.get(slug = slug)
    purchase = Purchase.objects.create(user = requset.user ,product = obj)
    requset.session["purchase_id"] = purchase.id
    number = random.randint(0 ,1)
    if number ==1:
        return HttpResponseRedirect("/purchase/success")
    return HttpResponseRedirect("/purchase/stopped/")

def purchase_success_view(requset):
    purchase_id = requset.session.get("purchase_id")
    purchase = Purchase.objects.get(id = purchase_id)
    purchase.completed = True
    purchase.save()
    return HttpResponse(f"Successfull {purchase_id}")

def purchase_stopped_view(requset):
    return HttpResponse("Stopped")