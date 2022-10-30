from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstarctUUID, AbstractTimeTracker


class Memory(AbstarctUUID, AbstractTimeTracker):
    size = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Size')
    )

    class Meta:
        verbose_name = 'Memory'
        verbose_name_plural = 'Memories'

    def __str__(self):
        return str(self.size)
