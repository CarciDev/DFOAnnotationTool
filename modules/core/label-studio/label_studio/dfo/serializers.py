from rest_framework import serializers
from .models import ZoomData

class ZoomDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoomData
        fields = ['zoom_position_x', 'zoom_position_y', 'zoom_scale', 'updated_at']