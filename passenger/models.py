from django.db import models


class Passenger(models.Model):
    passengerID = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16)

    def __str__(self):
        return self.name