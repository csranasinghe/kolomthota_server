from django.db import models

# Create your models here.

class Messages(models.Model):
    message_author = models.ForeignKey('accounts.Account', on_delete = models.PROTECT)
    message = models.CharField(max_length=200)
    is_reviewed = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now=True ,unique=True)
    def __str__(self):
        return str(self.created_time)

class VesselProgress(models.Model):
    vessel = models.ForeignKey('shipping_line.VesselArrival', on_delete=models.PROTECT, unique=True)
    dis = models.IntegerField(default=0)
    load = models.IntegerField(default=0)
    def __str__(self):
        return str(self.vessel)