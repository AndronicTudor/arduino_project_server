from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SensorDataSerializer
from ..models import SensorData


class ArduinoApiView(APIView):
    def get(self, request, format=None):
        return Response({"detail":"ABC"}, status=status.HTTP_200_OK)

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
            serializer.save()
            return Response({"detail": "Created succesful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArduinoGet(APIView):
    def get(self, request, slug, format=None):
        temps = SensorData.objects.filter(ard_id=slug).values_list('temp', flat=True)
        temp_max = max(temps)
        temp_min = min(temps)
        data = {'temp_max': temp_max, 'temp_min':temp_min }
        return Response(data, status.HTTP_200_OK)

