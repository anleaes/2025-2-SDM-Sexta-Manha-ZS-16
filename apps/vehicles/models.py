from django.db import models

# Create your models here.
class Vehicle(models.Model):
    license_plate = models.CharField('Placa', max_length=15, unique=True)
    model = models.CharField('Modelo', max_length=100)
    color = models.CharField('Cor', max_length=50)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        ordering = ['id']

    def __str__(self):
        return f'{self.license_plate} - {self.model}'