from django.urls import path
from .views import ArduinoApiView

urlpatterns = [
    path('arduino/', ArduinoApiView.as_view(), name='arduino-api'),
]