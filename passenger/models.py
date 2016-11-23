from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return self.user.first_name

    @receiver(post_save, sender=User)
    def create_user_passenger(sender, instance, created, **kwargs):
        if created:
            Passenger.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_passenger(sender, instance, **kwargs):
        instance.profile.save()