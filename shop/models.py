from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify  

# Create your models here.

User  = get_user_model()



class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True,null=True)
    slug = models.SlugField(blank=True)
    price = models.IntegerField(blank=True)
    pic = models.ImageField(upload_to="shop/PrP")
    des = models.TextField(blank=True)
    featured = models.BooleanField(default=False,blank=True)


    def __str__(self):
        return self.name
    

    def is_featured(self):
        return self.featured == True
    
    
    def save(self, *args, **kwargs):  # new
          if not self.slug:
              self.slug = slugify(self.name)
          return super(Product,self).save(*args, **kwargs)