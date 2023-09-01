import random

from decimal import Decimal
from django.core.management.base import BaseCommand
from hw_2_app.models import Client, Product, Order


class Command(BaseCommand):
    help = "Create order."

    # def add_arguments(self, parser):
    #     parser.add_argument('client', type=int, help='client ID')
    #     parser.add_argument('product', type=int, help='product ID')
    #     parser.add_argument('total_sum', type=float, help='Total sum')

    def handle(self, *args, **kwargs):
        client = Client.objects.get(pk=kwargs.get('client'))
        product = Product.objects.get(pk=kwargs.get('product'))
        total_sum = Order.objects.get(total_sum=kwargs.get(''))

        order = Order(client=client,
                      product=product,
                      total_sum=Decimal(total_sum))

        order.save()

        self.stdout.write(f'done, order pk = {order.pk}')
