from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product
# Create your models here.
User = get_user_model()


class Purchase(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, models.SET_NULL, null=True)
    completed = models.BooleanField(default=False)
    stripe_price = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def is_complete(self):
        return self.completed == True
    
    def __str__(self) -> str:
        return f"{self.product} by {self.user}"