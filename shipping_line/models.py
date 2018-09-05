from django.db import models


class ShippingLine(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class VesselDetails(models.Model):
    VESSEL_STATUS_CHOICES = (
        ('M', 'Main Line'),
        ('F', 'Feeder Line'),
    )
    vessel_name = models.CharField(max_length=200)
    shipping_agent = models.ForeignKey('accounts.ShippingAgent', on_delete=models.PROTECT)

    eta = models.DateTimeField()

    dis = models.IntegerField(default=0)
    load = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    loa_val = models.DecimalField(max_digits=6, decimal_places=2)
    vessel_status = models.CharField(choices=VESSEL_STATUS_CHOICES,  max_length=2)

    ref_no = models.CharField(max_length=100, unique=True)
    draft_arrival = models.DecimalField(max_digits=4, decimal_places=2)
    draft_departure = models.DecimalField(max_digits=4, decimal_places=2)
    remarks = models.TextField(null=True, blank=True)

    service = models.CharField(max_length=100, blank=True)

    last_port = models.CharField(max_length=100, default='')
    next_port = models.CharField(max_length=100, default='')

    modified_time = models.DateTimeField(auto_now_add=True)
    created_time = models.DateTimeField(auto_now=True)

    first_confirm = models.BooleanField(default=False)
    second_confirm = models.BooleanField(default=False)
    third_confirm = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Vessel Details'
        verbose_name_plural = 'Vessel Details'
        ordering = ['eta']

    def __str__(self):
        return str(self.vessel_name)

    @property
    def shipping_line(self):
        return self.shipping_agent.shipping_line

    @property
    def loa(self):
        return str(self.loa_val) + 'M'




