import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    university_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    gpa = models.FloatField()

    def __str__(self):
        return self.first_name +' '+self.last_name
