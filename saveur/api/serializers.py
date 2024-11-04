# restaurant/serializers.py
from rest_framework import serializers
from .models import Food, Drink, Reservation

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ["name", "description", "price", "image"]

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ["name", "description", "price", "image"]

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["name", "phone", "email", "guests", "date", "time"]