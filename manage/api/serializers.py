from rest_framework import serializers
from ..models import SensorData


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'
        lookup_field = 'ard_id'
        extra_kwargs = {
            'url': {'lookup_field': 'ard_id'}
        }

