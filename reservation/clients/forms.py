from django.forms import ModelForm
from .models import Client,ClientTypes,Product,Order


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class ClientTypesForm(ModelForm):
    class Meta:
        model = ClientTypes
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
