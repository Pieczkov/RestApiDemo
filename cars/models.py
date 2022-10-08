from django.db import models


class CarType(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    name = models.CharField(max_length=60)
    type = models.ForeignKey(CarType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} --> {self.type}"
