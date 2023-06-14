from django.db import models

class Apartment(models.Model):
    TYPE_CHOICES = (
        ('Apartment_Type: 1BHK', '1BHK'),
        ('Apartment_Type: 2BHK', '2BHK'),
        ('Apartment_Type: 3BHK', '3BHK'),
    )

    aprt_type = models.CharField(blank=True, max_length=20, choices=TYPE_CHOICES)
    picture = models.ImageField(blank=True)
    room_features = models.CharField(max_length=30)
    room_price = models.CharField(max_length=50, blank=True)
    location = models.CharField( max_length=100, default='Gaindakot,Nawalpur')
    description= models.TextField(blank=True)

    def __str__(self):
        return self.aprt_type
