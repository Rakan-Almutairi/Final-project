from django.db import models


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='product/images', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    confirm = models.IntegerField(null=True, blank=True)
    emp_create = models.ForeignKey('emp', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class emp(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    middile_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    pws = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    username = models.CharField(max_length=250, null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name

    @property
    def fullname(self):
        return self.first_name + self.middile_name + self.last_name
