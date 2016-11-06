# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import loader
from passenger import data
from django.template import RequestContext
from passenger import models
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SearchForm
from driver.models import Driver

def index(request):
    context = {}
    return render(request, 'passenger/index.html', context)
    #return HttpResponse("<h1>whaht</h1>")



class SearchFormView(View):
    form_class = SearchForm
    template_name = 'passenger/index.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.GET)
        found_entries = Driver.objects.filter(zoneFrom="\"zoneFrom\"").filter(zoneTo="\"zoneTo\"")

        context = {'found_entries':found_entries}
        return render(request, 'passenger/search_results.html', {'form': form}, context)




