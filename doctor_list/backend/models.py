from django.db import models

class Physicians(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

class Patient(models.Model):
    doctor = models.ForeignKey(Physicians, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
