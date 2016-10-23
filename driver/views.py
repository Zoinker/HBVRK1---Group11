# coding=utf-8
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>ghjgh.</h1>")
