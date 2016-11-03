# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = " "
    return render(request, 'passenger/index.html')
    #return HttpResponse("<h1>whaht</h1>")