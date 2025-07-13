from inflow.models import Inflow
from rest_framework import serializers


class InflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflow
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

    