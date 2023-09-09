import random

from django.core.management.base import BaseCommand
from hw_2_app.models import Client


class Command(BaseCommand):
    help = "Generate fake clients."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(first_name=f'Client{i}',
                            email='mail{i}@mail.ru',
                            phone=f'+7{i:09}',
                            address=f'City-{i}')
            client.save()
