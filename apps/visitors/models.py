from django.db import models

# Create your models here.
class Visitor(models.Model):
    first_name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)
    id_document = models.CharField('Documento (RG/CPF/Passaporte)', max_length=60, unique=True)
    phone = models.CharField('Telefone', max_length=30, blank=True, null=True)
    email = models.CharField('E-mail', max_length=254, blank=True, null=True)

    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitante'
        ordering = ['id']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.id_document}'