from django.urls import path

from .views import ArduinoApiView, ArduinoGet, ChartData, MapsData

urlpatterns = [
    path('arduino/', ArduinoApiView.as_view(), name='arduino-api'),
    path('chart-data/', ChartData.as_view(), name='chart-data'),
    path('maps-data/', MapsData.as_view(), name='maps-data'),
    path('arduino/<slug:slug>/', ArduinoGet.as_view(), name='get'),
]
