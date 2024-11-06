from django.contrib import admin

# Register your models here.
#newton10
#12345677

from django.contrib import admin
from .models import Food, Drink, Reservation

# Enregistrement des modèles dans l'administration

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')  # Affiche ces champs dans la liste des plats
    search_fields = ('name',)  # Permet de rechercher un plat par nom
    list_filter = ('price',)  # Ajoute un filtre par prix

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')  # Affiche ces champs dans la liste des boissons
    search_fields = ('name',)  # Permet de rechercher une boisson par nom
    list_filter = ('price',)  # Ajoute un filtre par prix

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'date', 'time', 'num_people_display')
    search_fields = ('name', 'email')  # Permet de rechercher une réservation par nom ou email
    list_filter = ('date',)  # Ajoute un filtre par date

    def num_people_display(self, obj):
        return obj.num_people  # ou tout autre calcul si `num_people` n'existe pas dans Reservation
    num_people_display.short_description = 'Number of People'
