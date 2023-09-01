from django.shortcuts import render
from django.http import HttpResponse

from hw_2_app.models import Client, Product, Order


def index(request):
    http = """
    <div class="task-block-teacher">
    
    <h1>Семинар 2</h1>
    <h4>Домашнее задание</h4>

    <p>Создайте три модели Django: клиент, товар и заказ. </p>
    
    <p>Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может 
    входить в несколько заказов. </p>
    
    <p>Поля модели «Клиент»:<br>
    — имя клиента<br>
    — электронная почта клиента<br>
    — номер телефона клиента<br>
    — адрес клиента<br>
    — дата регистрации клиента</p>
    
    <p>Поля модели «Товар»:<br>
    — название товара<br>
    — описание товара<br>
    — цена товара<br>
    — количество товара<br>
    — дата добавления товара</p>
    
    <p>Поля модели «Заказ»:<br>
    — связь с моделью «Клиент», указывает на клиента, сделавшего заказ<br>
    — связь с моделью «Товар», указывает на товары, входящие в заказ<br>
    — общая сумма заказа<br>
    — дата оформления заказа</p>
    
    <ul>
    <li>Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой ба</li>
    </ul>
</div>
    """
    return HttpResponse(http)


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
