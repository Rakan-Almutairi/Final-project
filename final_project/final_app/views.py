from django.shortcuts import render

from .models import Product, Category, emp


# Create your views here.

def home(request):
    title = 'Home Page'
    context = {'title': title}
    return render(request, 'home.html', context)


def products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'products.html', context)


def product(request, id):
    product = Product.objects.filter(id=id)
    context = {'product': product}
    return render(request, 'home.html', context)
