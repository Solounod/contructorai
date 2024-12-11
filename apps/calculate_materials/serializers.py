from rest_framework import serializers
from .models import PrompMainAi

class PrompMainAiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrompMainAi
        fields = '__all__'
