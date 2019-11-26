from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField, FloatField
from django.urls import reverse
import datetime
from datetime import timedelta, timezone


# Create your models here.

class Meal(models.Model):


    METRIC_TYPES = [
    ('kcal', 'kcal'),
    ('g', 'g'),
    ]

    time = models.DateTimeField(auto_now=True)
    jednostka = CharField(max_length=15, choices=METRIC_TYPES)
    poziom_cukru = models.PositiveSmallIntegerField()
    wrazliwosc = FloatField(default=1)    #ilość insuliny potrzebnej do obniżenia poziomu cukru o 100 mg/dl
    przelicznik = FloatField(default=1)   #ilość insuliny wbijanej na 100 kcal posiłku 
    weglowodany =  models.PositiveSmallIntegerField()
    bialka =  models.PositiveSmallIntegerField()
    tluszcze =  models.PositiveSmallIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    kalorycznosc = models.PositiveSmallIntegerField()
    insulin_dose = FloatField()
    bolus = models.CharField(max_length=50)
    warning = models.CharField(max_length=100, null=True)


    def get_absolute_url(self):
        return reverse('diet-home')


    def get_time_diff(self):
         timediff = timediff = datetime.datetime.now(timezone.utc) - self.time
         return timediff.total_seconds()


    def __str__(self):
        return "posiłek" + ": " + str(self.owner) + " " + str(self.time)


    class Meta:
        get_latest_by = "date"
