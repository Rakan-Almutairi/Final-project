from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput
from .models import Product
from django import forms


# Create the form class.
class ProductForm(ModelForm):
    # name1 = forms.CharField(max_length= 50)
    class Meta:
        model = Product
        fields = ('name', 'price', 'category', 'quantity', 'image', 'Created')

        widgets = {
            'name': TextInput(attrs={'class': 'custom-class', 'placeholder': 'الاسم هنا'})
        }
        labels = {
            'name': 'name for product'
        }
        help_texts = {
            'name': 'name for product must be string'
        }
        error_messages = {

        }

    def clean(self):
        cleaned_data = super(ProductForm, self).clean()
        name = cleaned_data.get('name')
        products = Product.objects.all()
        product_name = []
        for item in products:
            product_name.append(item.name)
        if name in product_name:
            self.add_error('name', 'this name is used')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class confirm(ModelForm):
    # name1 = forms.CharField(max_length= 50)
    class Meta:
        model = Product
        fields = ('confirm',)
