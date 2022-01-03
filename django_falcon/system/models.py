from django.db import models
from django.utils import timezone
from rest_framework import serializers


# Create your models here.


class SensorEvent(models.Model):

    name = models.CharField(max_length=128)
    value = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=16)
    status = models.CharField(max_length=16)

    lower_non_recoverable = models.FloatField(null=True, blank=True)
    lower_critical = models.FloatField(null=True, blank=True)
    lower_non_critical = models.FloatField(null=True, blank=True)
    upper_non_critical = models.FloatField(null=True, blank=True)
    upper_critical = models.FloatField(null=True, blank=True)
    upper_non_recoverable = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)


class SensorEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorEvent
        fields = '__all__'
