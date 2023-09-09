from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'sem3app/home.html', context)


# def home_task(request):
#     logger.info('Home task page -> access')
#     html = """
#             <div><h4>Задание</h4>
#             <p>Создайте пару представлений в вашем первом приложении:<br>
#             — главная<br>
#             — о себе.</p>
#             <p>Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и
#             данными о вашем первом Django-сайте и о вас.</p>
#             <ul>
#             <p>* Сохраняйте в логи данные о посещении страниц.</p>
#             </ul>
#             </div>
#             <a href="/hw/">Назад к домашней странице</a>
#     """
#     return HttpResponse(html)
