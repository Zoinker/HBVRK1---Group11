# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    context = {}
    return render(request, 'passenger/index.html', context)
    #return HttpResponse("<h1>whaht</h1>")