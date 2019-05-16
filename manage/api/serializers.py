from rest_framework import serializers
from ..models import SensorData


class SensorDataSerializer(serializers.Serializer):
    arduino_id = serializers.CharField(max_length=50, required=False)
    humidity = serializers.IntegerField(required=False)
    temperature = serializers.IntegerField(required=False)
    light = serializers.IntegerField(required=False)
    longitude = serializers.CharField(max_length=7, required=False)
    latitude = serializers.CharField(max_length=7, required=False)

    class Meta:
        model = SensorData
        fields = '__all__'
