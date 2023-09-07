from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView

from hw_3_app.models import Client, Product, Order


def index(request):
    html = """"""
    context = {
        'title': 'Главная страница',
        'data': 'Домашнее задание'
    }

    return render(request,
                  'hw_3_app/index.html',
                  context)


def about(request):
    context = {
        'title': 'About',
        'data': 'Текст страницы о нас'
    }

    return render(request,
                  'hw_3_app/about.html',
                  context)


def print_lst(lst):
    result = ''
    for res in lst:
        result += str(res) + '<br>'
    return result


def clients(request):
    return HttpResponse(print_lst(Client.objects.all()))


def products(request):
    return HttpResponse(print_lst(Product.objects.all()))


def orders(request):
    return HttpResponse(print_lst(Order.objects.all()))


# Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
# — за последние 7 дней (неделю)
# — за последние 30 дней (месяц)
# — за последние 365 дней (год)
#
# Товары в списке не должны повторятся.
class ProductsFromOrders(ListView):
    model = Order
    template_name = 'hw_3_app/product_orders_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = Client.objects.get(pk=self.kwargs['pk'])
        order = Order.objects.filter(client=client).all()
        context['order'] = order
        context['title'] = f'Заказы клиента {client}'
        return context
