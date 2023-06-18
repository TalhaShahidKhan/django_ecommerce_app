from django.shortcuts import render,redirect
from shop.models import Product,Store
from django.contrib.auth.decorators import login_required
from shop.forms import ProdutCreateForm,StoreCreateForm
# Create your views here.
def list_product_view(request):
    prod = Product.objects.all()
    store = Store.objects.all()
    context = {
        "pro":prod,
        "sto":store
    }
    return render(request,"shop/listprod.html",context)



@login_required(login_url='login')
def create_product_view(request):
  form=ProdutCreateForm()
  context={
    "form":form
  }
  if request.method =="POST":
    form=ProdutCreateForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect("/shop")
  return render(request, 'shop/addprod.html',context)


@login_required(login_url='login')
def create_store_view(request):
  form=StoreCreateForm()
  context={
    "form":form
  }
  if request.method =="POST":
    form=StoreCreateForm(request.POST, request.FILES)
    if form.is_valid():
      store = form.save(commit=False)
      store.author = request.user
      store.save()
      return redirect("/shop")
  return render(request, 'shop/addstore.html',context)