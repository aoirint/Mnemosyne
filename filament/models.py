from django.db import models

# Create your models here.
FILAMENT_MATERIAL_CHOICES = (
    ( 'PLA', 'PLA' ),
    ( 'ABS', 'ABS' ),
    ( 'TPU', 'TPU' ),
)

class Filament(models.Model):
    material = models.TextField(choices=FILAMENT_MATERIAL_CHOICES)
    amount = models.IntegerField()
    price = models.IntegerField()
    shop = models.TextField()
    url = models.URLField()
    owner = models.TextField()
    name = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
