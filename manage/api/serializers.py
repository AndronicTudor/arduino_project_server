from rest_framework import serializers
from ..models import SensorData


class SensorDataSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=50, required=False)
    hum = serializers.IntegerField(required=False)
    temp = serializers.IntegerField(required=False)
    lig = serializers.IntegerField(required=False)
    lat = serializers.CharField(max_length=7, required=False)
    lon = serializers.CharField(max_length=7, required=False)

    class Meta:
        model = SensorData
        fields = ('id', 'hum', 'temp', 'lig', 'lat', 'lon')
