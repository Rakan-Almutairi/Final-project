from django.contrib.auth import authenticate, login, check_group
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import ProductForm, SignUpForm, confirm
from .models import Product
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group


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


@login_required
@check_group('Employee')
def add_product(request):
    form = ProductForm
    if request.method == 'POST':
        form = form(request.POST, request.FILES)
        if form.is_valid():
            print(form.errors)
            form.save()
        print("this is post page")
    context = {'form': form}
    return render(request, 'add-product.html', context)


@login_required
@check_group('Employee')
def delete_product(request, id):
    obj = Product.objects.filter(id=id)
    obj.delete()
    return HttpResponseRedirect(reverse('products'))
    context = {}
    return render(request, 'delete_product.html', context)


@login_required
@check_group('Employee')
def update_product(request, id):
    form = ProductForm(instance=Product.objects.filter(id=id).first())
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            print(form.errors)
            form.save()
    context = {'form': form}
    return render(request, 'update-product.html', context)


@login_required
@check_group('Manger')
def Confirm(request, id):
    form = confirm(instance=Product.objects.filter(id=id).first())
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            print(form.errors)
            form.save()
    context = {'form': form, 'product': Product.objects.filter(id=id)}
    return render(request, 'Confirm-Product.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('product')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# def confirm(request, id):
#     form = confirm(instance=Product.objects.filter(id=id).first())
#     if request.method == 'POST':
#         form = form(request.POST)
#         if form.is_valid():
#             print(form.errors)
#             form.save()
#     context = {'form': form}
#     return render(request, 'Confirm-Product.html', context)
