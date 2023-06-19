from django import forms
from shop.models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","price","des","pic"]