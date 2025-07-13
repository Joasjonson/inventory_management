from rest_framework import serializers
from outflow.models import Outflow


class OutflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Outflow
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')