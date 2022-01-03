from django.contrib import admin
from .models import SensorEvent


# Register your models here.


@admin.register(SensorEvent)
class SensorEventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'value', 'unit', 'status', 'timestamp']
    list_filter = ['name', 'unit']
    search_fields = ['name', 'unit', 'timestamp']
