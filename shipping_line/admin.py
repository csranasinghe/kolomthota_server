from django.contrib import admin
from .models import ShippingLine, VesselArrival, Vessel

admin.site.register(ShippingLine)
admin.site.register(Vessel)
admin.site.register(VesselArrival)

