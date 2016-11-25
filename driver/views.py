# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from driver.models import Driver


def index(request):
    return render(request, './driver/index.html')


def become_driver(request):
    user = request.user
    Driver.objects.create_driver(user)
    return render(request, './driver/index.html')


