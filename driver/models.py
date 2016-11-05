import json

from django.db import models

from passenger.models import Passenger


class Driver(models.Model):
    name = models.CharField(max_length=50)
    isActive = models.BooleanField(default=False)
    isBusy = models.BooleanField(default=False)
    zones = models.CharField(max_length=1000, blank=True)
    phone_number = models.CharField(max_length=16)
    requests = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

    def set_requests(self, request_list):
        self.requests = json.dumps(request_list)

    def get_requests(self):
        return json.loads(self.requests)

    def set_zones(self, zones_list):
        self.zones = json.dumps(zones_list)

    def get_zones(self):
        return json.loads(self.zones)


class Zone(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Request(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    driver = models.ManyToManyField(Driver)
    inTown = models.BooleanField(default=True)
    destination = models.ForeignKey(Zone)
    arrivalTime = models.DateTimeField()
    status = models.CharField(max_length=16, default="pending")

    def __str__(self):
        return "Frá " + self.passenger.name
