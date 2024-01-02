from django.urls import path
from . import views

urlpatterns = [
    path("clients/", views.clients, name="clients"),
    path("info/", views.info, name="info"),
    path("add/", views.add, name="add"),
    path("product/", views.addProduct, name="product"),
    path("order/", views.order, name="order"),
    path("cType", views.cType, name="cType"),



]
