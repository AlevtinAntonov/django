from django.shortcuts import render
import logging
from django.http import HttpResponse
from random import randint

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Seminar 1 task 5")


def head_tails(request):
    result = 'HEADS' if randint(0, 1) else 'TAILS'
    logger.info(f'head-tails {result=}')
    return HttpResponse(result)


def cube(request):
    result = randint(1, 6)
    logger.info(f'cube {result=}')
    return HttpResponse(result)


def rand_num(request):
    result = randint(1, 100)
    logger.info(f'random number {result=}')
    return HttpResponse(result)
