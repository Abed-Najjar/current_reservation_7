from django.shortcuts import render
from .forms import ClientForm,ClientTypesForm,ProductForm,OrderForm
from django.http import HttpResponse
from django.views import View


CATEGORY = ["Food", "Snacks", "Drinks", "Hardware"]


def clients(request):
    form = ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "clients.html", {'form':form})


def info(request):
    return render(request, "info.html")


def add(request):
    return render(request, "add.html")


def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            return render(request, "product.html", {'form': form})


    return render(request, "product.html", {'form':form})


def order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            return render(request, "order.html", {'form': form})

    return render(request, "order.html", {'form': form})

def cType(request):
    form = ClientTypesForm()
    if request.method == 'POST':
        form = ClientTypesForm(request.POST)
        if form.is_valid():
            return render(request, "cType.html", {'form': form})

    return render(request, "cType.html", {'form': form})