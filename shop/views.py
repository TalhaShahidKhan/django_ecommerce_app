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




def post_details(request,slug):
  post=Product.objects.get(slug=slug)
  context={
    "post":post
  }
  return render(request,'shop/prodet.html',context)




@login_required(login_url='login')
def create_post(request):
  form=ProductCreateForm()
  context={
    "form":form
  }
  if request.method =="POST":
    form=ProductCreateForm(request.POST, request.FILES)
    if form.is_valid():
      post =form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect("/blog")
  return render(request, 'blog/addpost.html',context)







@login_required(login_url='login')
def update_post(request,slug):
  post=Product.objects.get(slug=slug)
  form=ProductCreateForm(instance=post)
  context={
    "form":form,
  }
  if not post.can_edit(request.user):
        messages.error(request,"You don't have permission to update others post")
        return redirect('/blog')
  if request.method == "POST" :
    form=ProductCreateForm(request.POST, instance=post, files=request.FILES)
    if form.is_valid():
      post =form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect("/blog")

  return render(request, "blog/updatepost.html",context)

@login_required(login_url='login')
def delt_post(request,slug):
  post=Product.objects.get(slug=slug)
  if not post.can_edit(request.user):
        messages.error(request,"You don't have permission to delete others post")
        return redirect('/blog')
  else:
    post.delete()
  return render(request, 'blog/dltpost.html')

