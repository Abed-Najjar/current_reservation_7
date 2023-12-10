from django.urls import path
from . import views

urlpatterns = [
    path("", views.clients, name="clients"),
    path("info/", views.info, name="info"),
    path("add/", views.add, name="add"),
    path("product/", views.addProduct, name="product"),
    path("product_class", views.ProductView.as_view(), name="product_class"),

]
