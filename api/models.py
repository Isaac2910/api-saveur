from django.db import models

from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def _str_(self):
        return self.name

class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def _str_(self):
        return self.name

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    
    def _str_(self):
        return f"Reservation by {self.name} on {self.date} at {self.time}"
    
<<<<<<< HEAD:saveur/api/models.py
###les tables ajouters

class Breakfast(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='breakfast_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Dessert(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='dessert_images/', null=True, blank=True)

    def __str__(self):
        return self.name
=======
    #postgresql://sav_gk4d_user:gxAEMjs30Sq0O2Htiu9N530ySUXrdzGq@dpg-cskv6uqj1k6c73bo8bb0-
>>>>>>> 6b079d313befb77ed7060144786fe497ec3cf4fb:api/models.py
