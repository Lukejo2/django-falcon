from django.urls import path
from . import api


urlpatterns = [
    path('sensor/event', api.SensorEventListView.as_view()),
    path('sensor/event/<int:pk>', api.SensorEventView.as_view())
]
