from django  import forms
from shop.models import Product,Store


class ProdutCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","store","des","pic","price"]

class StoreCreateForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["name","cover","details"]