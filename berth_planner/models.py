from django.db import models


class Berth(models.Model):
    name = models.CharField(max_length=10)
    max_length = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    max_across = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    max_draft = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'berth'
        verbose_name_plural = 'berths'

    def __str__(self):
        return str(self.name)


class BerthAllocation(models.Model):
    berth = models.ForeignKey('berth_planner.Berth', )