import random

from decimal import Decimal
from django.core.management.base import BaseCommand
from hw_2_app.models import Client, Product, Order


class Command(BaseCommand):
    help = "Generate fake orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for c in Client.objects.all():
            for p in Product.objects.all():
                for i in range(1, count + 1):
                    order = Order(client=c,
                                  product=p,
                                  total_sum=Decimal(random.randint(1, 1000)))
                order.save()