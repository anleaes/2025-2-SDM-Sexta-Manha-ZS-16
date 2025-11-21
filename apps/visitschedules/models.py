from django.db import models
from visitors.models import Visitor
from vehicles.models import Vehicle
from departments.models import Department  # será criado futuramente
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class VisitSchedule(models.Model):
    visitor = models.ForeignKey(
        Visitor,
        on_delete=models.CASCADE,
        related_name='visit_schedules'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='visit_schedules'
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        related_name='visit_schedules',
        null=True, blank=True
    )
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='managed_visit_schedules'
    )

    scheduled_datetime = models.DateTimeField('Data/Hora Agendada')
    status = models.CharField('Status', max_length=50)

    class Meta:
        verbose_name = 'Agendamento de Visita'
        verbose_name_plural = 'Agendamentos de Visita'
        ordering = ['scheduled_datetime']

    def __str__(self):
        return f'Visita de {self.visitor} em {self.scheduled_datetime}'