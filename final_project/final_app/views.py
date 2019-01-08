from django.shortcuts import render, get_object_or_404

from .forms import ProductForm
from .models import Product


# Create your views here.

def home(request):
    title = 'Home Page'
    context = {'title': title}
    return render(request, 'home.html', context)


def products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'products.html', context)


def product(request, id):
    context = {'product': Product.objects.filter(id=id)}
    return render(request, 'home.html', context)


def add_product(request):
    form = ProductForm
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            print(form.errors)
            instance = form.save(commit=False)
            instance.confirm = 0
            instance.save()
        print("this is post page")
    context = {'form': form}
    return render(request, 'add-product.html', context)


def delete_product(request, id):
    form = Product.objects.filter(id=id).first()
    if request.method == 'POST':
        form.delete()
        print("this is post page")
    context = {'form': form, 'product': Product.objects.filter(id=id)}
    return render(request, 'delete.html', context)


def update_product(request, id):
    form = ProductForm(instance=Product.objects.filter(id=id).first())
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            print(form.errors)
            form.save()
    context = {'form': form}
    return render(request, 'update-product.html', context)
