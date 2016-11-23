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
import logging

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

        form = self.form_class(request.POST)
        if form.is_valid():
            zone_from = form.cleaned_data['zoneFrom']
            zone_to = form.cleaned_data['zoneTo']
            logging.warning(zone_to)
            found_entries = Driver.objects.filter(zoneFrom=zone_from).filter(zoneTo=zone_to)

            context = {'found_entries':found_entries}
            logging.warning(context)
            return render(request, 'passenger/search_results.html', {'form': form}, context)




