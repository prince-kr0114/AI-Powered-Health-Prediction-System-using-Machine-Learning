from django.db import models

# Create your models here.

from django.db import models


class HealthPrediction(models.Model):

    age = models.IntegerField()

    gender = models.CharField(max_length=20)

    height = models.FloatField()

    weight = models.FloatField()

    blood_pressure = models.FloatField()

    cholesterol = models.FloatField()

    prediction = models.CharField(max_length=50)

    confidence = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.age} - {self.prediction}"