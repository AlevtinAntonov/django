from random import choices
from django.core.management.base import BaseCommand
from myapp3.models import Author, Post

LOREM = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras gravida leo non consequat ullamcorper. Donec "
         "non tempus massa. In sodales, magna vitae cursus lacinia, erat leo dapibus odio, non pellentesque odio urna "
         "at nisl. In porttitor sapien dolor, non consequat metus posuere non. Nunc eleifend nisi dapibus blandit "
         "mattis. Nam id fermentum magna. Nunc ornare ipsum eget justo fringilla interdum. Pellentesque non "
         "sollicitudin ante, vel ullamcorper lorem. Aliquam lacinia tincidunt risus, eget pulvinar mi pretium "
         "tincidunt. Sed ut nisl laoreet, posuere massa ut, rutrum arcu. Integer volutpat urna at lorem iaculis, "
         "in faucibus augue condimentum. Suspendisse laoreet lacus vestibulum varius varius. In efficitur mauris "
         "ante, a commodo quam bibendum quis. Curabitur tristique nunc ut tellus dictum euismod. Sed rhoncus quis "
         "tortor vitae efficitur. Fusce sed nunc ante. Duis ornare suscipit velit, eget eleifend ante tristique sed. "
         "Etiam lobortis tortor sit amet porta bibendum. Quisque nisl arcu, finibus non sollicitudin in, maximus sed "
         "purus. Donec tristique ex sem, vestibulum malesuada ante tempor nec. Praesent non mi elementum, "
         "dignissim nunc eu, sollicitudin justo. Fusce metus ante, consectetur sed eleifend sed, tempus at purus. "
         "Integer ut velit finibus, egestas tortor sed, sodales enim. Mauris sem dui, posuere ut volutpat in, "
         "posuere quis ipsum.")


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}',
                            email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=64)),
                    author=author
                )
                post.save()
