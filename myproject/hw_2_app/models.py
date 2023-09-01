from django.db import models
from django.db.models import Manager


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date_registration = models.DateField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} - {self.email} - {self.date_registration}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date_add_product = models.DateTimeField(auto_now_add=False)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.price} - {self.description}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    total_sum = models.DecimalField(max_digits=7, decimal_places=2)
    date_of_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} - {self.product} - {self.total_sum}'
