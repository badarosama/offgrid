from django.db import models
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    freq = models.IntegerField()

    
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    vendors = models.ForeignKey(Vendor)






