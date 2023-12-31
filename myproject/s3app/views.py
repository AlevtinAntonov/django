from random import randint

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from s3app.models import GameModel, Author, Post


def index(request):
    context = {
        'title': 'Главная страница',
        'data': 'Текст главной страницы'
    }

    return render(request,
                  's3app/index.html',
                  context)


def about(request):
    context = {
        'title': 'Главная страница',
        'data': 'Текст страницы о нас'
    }

    return render(request,
                  's3app/about.html',
                  context)


class GameView(TemplateView):
    template_name = 's3app/game.html'


class HeadsGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [('TAILS', 'HEADS')[randint(0, 1)] for i in range(self.kwargs['count'])]
        context['results'] = results
        context['title'] = 'Игра в Орла и Решку'
        return context


class DiceGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [randint(1, 6) for i in range(self.kwargs['count'])]
        context['results'] = results
        context['title'] = 'Игра в кости'
        return context


class AllArticlesView(TemplateView):
    template_name = 's3app/articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.get(pk=self.kwargs['pk'])
        posts = Post.objects.filter(author=author).all()
        context['posts'] = posts
        context['title'] = f'Посты автора {author}'
        return context


class ArticlePage(DetailView):
    model = Post
    template_name = 's3app/article_page.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj


def heads(request):
    result = ('TAILS', 'HEADS')[randint(0, 1)]

    game = GameModel(result=result)
    game.save()

    return HttpResponse(f'{game}')


def last_games(request):
    last = GameModel().return_last(5)
    last_str = ['<br>' + str(i) for i in last]
    return HttpResponse(last_str)


def authors(request):
    res = Author.objects.all()
    print(res)
    res1 = ''
    for i in res:
        res1 += str(i) + '<br>'
    return HttpResponse(f'{res1}')