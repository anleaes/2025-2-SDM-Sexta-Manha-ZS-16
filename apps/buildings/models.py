from django.db import models

# Create your models here.
class Building(models.Model):
    name = models.CharField('Nome', max_length=150)
    address = models.CharField('Endereço', max_length=255)
    description = models.TextField('Descrição', blank=True, null=True)
    operational_status = models.CharField('Status Operacional', max_length=50)
