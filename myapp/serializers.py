
from rest_framework import serializers
from .models import Purchase, Sales, Adjust

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class AdjustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adjust
        fields = '__all__'
