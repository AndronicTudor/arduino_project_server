from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SensorDataSerializer
from ..models import SensorData


class ArduinoApiView(APIView):

    def post(self, request, format=None):
        data = request.data
        if data.get('hum'):
            data['hum'] = int(data['hum'])
        if data.get('temp'):
            data['temp'] = int(data['temp'])
        if data.get('lig'):
            data['lig'] = int(data['lig'])
        serializer = SensorDataSerializer(data=data)
        if serializer.is_valid():
            if data.get('update'):
                query = SensorData.objects.filter(
                                            ard_id=data.get('ard_id'))\
                                            .order_by('-created').first()
                query.lat = data.get('lat')
                query.lon = data.get('lon')
                query.save()
                return Response({"detail": "Update succesful"},
                                status=status.HTTP_200_OK)
            else:
                serializer.save()
                return Response({"detail": "Created succesful"},
                                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArduinoGet(APIView):

    def get(self, request, slug, format=None):
        temps = SensorData.objects.filter(ard_id=slug)\
                                  .values_list('temp', flat=True)
        temp_max = max(temps)
        temp_min = min(temps)
        data = {'temp_max': temp_max, 'temp_min':temp_min }
        return Response(data, status.HTTP_200_OK)


class ChartData(APIView):

    def get(self, request,  format=None):
        labels = ['Temperature max', 'Temperature min', 'Humidity max',
                  'Humidity min', 'Light max', 'Light min']
        data = SensorData.objects.filter().values('temp', 'hum', 'lig')
        temp = []
        hum = []
        lig = []
        for d in data:
            temp.append(d.get('temp'))
            hum.append(d.get('hum'))
            lig.append(d.get('lig'))
        sensor_data = [max(temp), min(temp), max(hum), min(hum),
                       max(lig), min(lig)]
        data = {'labels': labels, 'sensor_data': sensor_data}
        return Response(data, status.HTTP_200_OK)

class MapsData(APIView):

    def get(self, request,  format=None):
        data = SensorData.objects.filter().values('lat', 'lon')
        gps_data = []
        for d in data:
            gps_data.append({'lat': float(d.get('lat')), 'lng': float(d.get('lon'))})
        data = {'gps_data': gps_data}
        return Response(data, status.HTTP_200_OK)
