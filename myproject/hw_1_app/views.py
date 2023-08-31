from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Homework index page -> access')
    html = """<!DOCTYPE html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Домашнее задание №1</title>
                    <meta property="og:title" content="Заголовок страницы в OG">
                    <meta property="og:description" content="Описание страницы в OG">
                  </head>
                  <body>
                    <header>
                      <h1>Фреймворк Django (семинары)</h1>
                      <p>Урок 1. Первое Знакомство с Django</p>
                      <nav>
                        <ul>
                          <li><a href="">Эта страница</a></li>
                          <li><a href="https://gbcdn.mrgcdn.ru/uploads/asset/5443291/attachment/b2095e4dad984ea3734b332f31c4779e.pdf">
                          Страница с Презентацией</a></li>
                          <li><a href="home_task/">Страница с Домашним заданием</a></li>
                        </ul>
                      </nav>
                    </header>
                    <main>
                      <article>
                        <section>
                          <h2>Наш преподаватель</h2>
                          <p>Станислав Никуличев</p>
                          <img src="https://gbcdn.mrgcdn.ru/uploads/avatar/4251569/attachment/thumb-5d6aa33681155c23fd3a66f784f57baf.png" alt="Станислав Никуличев">
                          <p>GeekBrains</p>
                        </section>
                        <section>
                          <h2>Описание семинара</h2>
                          <p>На этом семинаре мы:</br>
                          <li>научимся установке и настройке для первого запуска;</li>
                          <li>изучим структуру проекта и работу с ним;</li>
                          <li>узнаем о приложениях как частях проекта;</li>
                          <li>изучить настройки логирования в Django.</p></li>
                        </section>
                      </article>
                    </main>
                    <footer>
                      <a href="https://gb.ru/">GeekBrains - образовательный портал</a>
                    </footer>
                  </body>
                </html>"""
    return HttpResponse(html)


def home_task(request):
    logger.info('Home task page -> access')
    html = """
            <div><h4>Задание</h4>
            <p>Создайте пару представлений в вашем первом приложении:<br>
            — главная<br>
            — о себе.</p>
            <p>Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и 
            данными о вашем первом Django-сайте и о вас.</p>
            <ul>
            <p>* Сохраняйте в логи данные о посещении страниц.</p>
            </ul>
            </div>
            <a href="/hw/">Назад к домашней странице</a>
    """
    return HttpResponse(html)
