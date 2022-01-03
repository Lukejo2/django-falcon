from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from .models import SensorEvent, SensorEventSerializer


class SensorEventListView(generics.ListCreateAPIView):
    queryset = SensorEvent.objects.all()
    serializer_class = SensorEventSerializer
    filterset_fields = '__all__'
    search_fields = ['name', 'unit', 'status', 'timestamp']
    ordering_fields = '__all__'
    ordering = ['-timestamp', 'name']


class SensorEventView(generics.RetrieveUpdateAPIView):
    queryset = SensorEvent.objects.all()
    serializer_class = SensorEventSerializer
