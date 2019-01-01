from django.shortcuts import render

from .forms import ProductForm
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


def add_product(request):
    form = ProductForm
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            print(form.errors)
            instance = form.save(commit=False)
            instance.quantity = 90
            instance.save()
        print("this is post page")
    context = {'form': form}
    return render(request, 'add-product.html', context)
