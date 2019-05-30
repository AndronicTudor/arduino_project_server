from django.db import models
from django.utils.translation import gettext_lazy as _


class SensorData(models.Model):
    arduino_id = models.CharField(max_length=50, verbose_name=_("Arduino device id"))
    humidity = models.IntegerField()
    temperature = models.IntegerField()
    light = models.IntegerField()
    longitude = models.CharField(max_length=7)
    latitude = models.CharField(max_length=7)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.arduino_id}-{self.created}"
