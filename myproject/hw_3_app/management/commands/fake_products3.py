import random

from django.core.management.base import BaseCommand
from hw_3_app.models import Product
from decimal import Decimal


class Command(BaseCommand):
    help = "Generate fake productss."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'Product{i}',
                              description=f'Product description - {i}',
                              price=Decimal(f'{random.randint(10, 999)}.{i}{i}'),
                              date_add_product=f'2023-09-06')
            product.save()
