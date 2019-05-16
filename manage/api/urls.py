from django.urls import path
from .views import ArduinoApiView, ArduinoGet

urlpatterns = [
    path('arduino/', ArduinoApiView.as_view(), name='arduino-api'),
    path('arduino/<slug:slug>/', ArduinoGet.as_view(), name='get'),
]