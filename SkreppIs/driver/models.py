from django.db import models
import json


class Driver(models.Model):
    driverID = models.BigIntegerField()
    name = models.CharField(max_length=50)
    isActive = models.BooleanField(default=False)
    isBusy = models.BooleanField(default=False)
    zones = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=16)
    requests = models.CharField(max_length=1000)

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
    passengerID = models.BigIntegerField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    inTown = models.BooleanField(default=True)
    destination = models.ForeignKey(Zone)
    arrivalTime = models.DateTimeField()
    status = models.CharField(max_length=16, default="pending")

    def __str__(self):
        return self.driver.name + " " + str(self.passengerID)


# Create your models here.
