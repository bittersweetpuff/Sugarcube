from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from datetime import timedelta, timezone


# Create your models here.

class SugarLevel(models.Model):

    time = models.DateTimeField(auto_now=True)
    sugarlevel = models.PositiveSmallIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    warning = models.CharField(max_length=100)
    trend = models.CharField(max_length=50)


    def get_absolute_url(self):
        return reverse('sugar-home')


    def get_time_diff(self):
         timediff = timediff = datetime.datetime.now(timezone.utc) - self.time
         return timediff.total_seconds()


    def __str__(self):
        return str(self.sugarlevel) + ": " + str(self.owner) + " " + str(self.time)

    class Meta:
        get_latest_by = "date"
