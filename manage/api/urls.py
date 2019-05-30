from django.urls import path

from .views import ArduinoApiView, ArduinoGet, ChartData

urlpatterns = [
    path('arduino/', ArduinoApiView.as_view(), name='arduino-api'),
    path('chart-data/', ChartData.as_view(), name='chart-data'),
    path('arduino/<slug:slug>/', ArduinoGet.as_view(), name='get'),
  