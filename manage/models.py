from django.db import models
from django.utils.translation import gettext_lazy as _


class SensorData(models.Model):
    ard_id = models.CharField(max_length=50, verbose_name=_("Arduino device id"))
    hum = models.IntegerField(null=True, blank=True)
    temp = models.IntegerField(null=True, blank=True)
    lig = models.IntegerField(null=True, blank=True)
    lat = models.CharField(max_length=7, null=True, blank=True)
    lon = models.CharField(max_length=7, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ard_id}-{self.created.strftime('%m/%d/%Y, %H:%M:%S')}"
