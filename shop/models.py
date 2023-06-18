from django.db import models
from django.template.defaultfilters import slugify  
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class Store(models.Model):
  author = models.OneToOneField(User , on_delete=models.CASCADE,null=True,blank=True)
  name=models.CharField(max_length=50,blank=True)
  slug = models.SlugField(unique=True, blank=True, null=True)
  details = models.TextField(blank=True)
  cover = models.ImageField(upload_to="shop/cov")

  class Meta:
      ordering = ['-name']

  
  def __str__(self) :
    return self.name
  
  def save(self,*args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    return super(Store,self).save(*args, **kwargs)
  



class Product(models.Model):
  store = models.OneToOneField(Store , on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=20,blank=True)
  des  = models.TextField(blank=True)
  slug = models.SlugField(unique=True, blank=True, null=True)
  pic = models.ImageField(upload_to='shop/PrP')
  price = models.IntegerField(blank=True)
  featured = models.BooleanField(default=False, blank=True)
  created_at = models.DateTimeField(auto_now_add=True,blank = True,null=True)
  updated_at = models.DateTimeField(auto_now=True,blank = True,null=True)

  class Meta:
      ordering = ['-created_at']


  def is_featured(self):
    return self.featured == True
  
  def __str__(self) :
    return self.name
  

  def save(self,*args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    return super(Product,self).save(*args, **kwargs)
  
  
