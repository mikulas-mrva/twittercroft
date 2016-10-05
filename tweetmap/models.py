from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=60)
    code = models.CharField(max_length=3)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
