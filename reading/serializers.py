from rest_framework import serializers
from .models import Reading

class ElpaSerializer(serializers.ModelSerializer):
    class Meta:
        model =Reading
        fields = ['reading_id','BPNumber','fullname','accNumber','meterReading','created_at']
        
        