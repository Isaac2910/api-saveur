from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Food, Drink, Reservation
from .serializers import FoodSerializer, DrinkSerializer, ReservationSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdminUser()]
        return [AllowAny()]

class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdminUser()]
        return [AllowAny()]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [AllowAny]