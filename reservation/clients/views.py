from django.shortcuts import render
from .forms import Product
from django.http import HttpResponse
from django.views import View


CATEGORY = ["Food", "Snacks", "Drinks", "Hardware"]


def clients(request):
    return render(request, "clients.html", {})


def info(request):
    return render(request, "info.html")


def add(request):
    return render(request, "add.html")


def addProduct(request):

    if request.method == 'POST':
        form = Product(request.POST)

        if form.is_valid():
            return render(request, "product.html", {'form': form})

    else:
        return render(request, "product.html")


class ProductView(View):

    def get(self, request):
        form = Product()
        return render(request, "product.html",{'form': form})

    def post(self, request):
        form = Product(request.POST)
        num_products = request.session.get('num_products', 0) + 1
        request.session['num_products'] = num_products

        if form.is_valid():
            return render(request, "product.html", {'form': form})
