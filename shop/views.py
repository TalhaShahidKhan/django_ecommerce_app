from django.shortcuts import render,redirect
from shop.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shop.forms import ProductCreateForm
# Create your views here.
 

def list_product_view(request):
    product = Product.objects.all()
    context = {
        "pro":product
    }
    return render(request,  "shop/listprod.html",context)




def product_details_view(request,slug):
  product=Product.objects.get(slug=slug)
  context={
    "pro":product
  }
  return render(request,'shop/prodet.html',context)




@login_required(login_url='login')
def create_product_view(request):
  form=ProductCreateForm()
  context={
    "form":form
  }
  if request.method =="POST":
    form=ProductCreateForm(request.POST, request.FILES)
    if form.is_valid():
      pro =form.save(commit=False)
      pro.author = request.user
      pro.save()
      return redirect("/shop")
  return render(request, 'shop/addprod.html',context)







@login_required(login_url='login')
def update_product_view(request,slug):
  product=Product.objects.get(slug=slug)
  form=ProductCreateForm(instance=product)
  context={
    "form":form,
  }
  if request.method == "POST" :
    form=ProductCreateForm(request.POST, instance=product, files=request.FILES)
    if form.is_valid():
      product =form.save(commit=False)
      product.author = request.user
      product.save()
      return redirect("/shop")

  return render(request, "shop/updpro.html",context)

@login_required(login_url='login')
def delt_product(request,slug):
  product=Product.objects.get(slug=slug)
  product.delete()
  return render(request, 'shop/dltpro.html')
