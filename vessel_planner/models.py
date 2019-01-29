from django.db import models
from shipping_line.models import VesselArrival
# Create your models here.



class VesselProgress(models.Model):
    vessel = models.OneToOneField(VesselArrival, on_delete=models.CASCADE ,unique =True)
    dis = models.IntegerField(default=0)
    load = models.IntegerField(default=0)
    def __str__(self):
        return str(self.vessel)

    @property
    def vessel_shipping_line(self):
        return self.vessel.shipping_agent.shipping_line