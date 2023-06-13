from django.db import models
# Create your models here.



class Product(models.Model):
  name = models.CharField(max_length=20,blank=True)
  des  = models.TextField(blank=True)
  pic = models.ImageField(upload_to='shop/PrP')
  price = models.IntegerField(blank=True)
  featured = models.BooleanField(default=False, blank=True)


  def is_featured(self):
    return self.featured == True
  

class Store(models.Model):
  product = models.OneToOneField(Product,on_delete=models.CASCADE)
  name=models.CharField(max_length=50,blank=True)
  details = models.TextField(blank=True)
  cover = models.ImageField(upload_to="shop/cov")
