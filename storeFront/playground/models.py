from django.db import models

class Car(models.Model):
    car_name = models.CharField(max_length=15)
    car_speed = models.IntegerField(default=40)

    def __str__(self):
        return self.car_name