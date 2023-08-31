from django.db import models
from django.db.models import Manager


class GameModel(models.Model):
    result = models.CharField(max_length=10)
    played = models.DateTimeField(auto_now_add=True)

    objects = Manager()

    def __str__(self):
        return f'Результат игры: {self.result}, время: {self.played}'

    class Meta:
        ordering = ['-played']

    @staticmethod
    def return_last(n):
        return GameModel.objects.all()[:n]


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(max_length=1000)
    bd = models.DateField()

    def __str__(self):
        return f'{self.name} {self.surname}'


class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField(max_length=1000)
    publish_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    views = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author} - {self.title} - {self.publish}'
