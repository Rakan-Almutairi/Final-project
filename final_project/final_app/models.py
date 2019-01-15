from django.db import models

from django.contrib.auth.models import User, Group


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='product/images', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    confirm = models.BooleanField(null=False, blank=True, default=False)
    Created = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class emp(models.Model):
#     User = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def in_group(self):
#         return Group.object.all()
