from rest_framework import serializers
# from rest_framework import trade
from .models import trade

class tradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = trade
        fields = '__all__'
        