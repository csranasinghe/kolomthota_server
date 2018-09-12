from django.forms import ModelForm  
from .models import ShippingLine, VesselArrival,Vessel


class VesselArrivalDetailsForm(ModelForm):
    class Meta:
        model = VesselArrival
        exclude = [
            'first_confirm',
            'second_confirm',
            'third_confirm',
            'modified_time',
            'created_time'
        ]

class VesselDetailsForm(ModelForm):
    class Meta:
        model = Vessel
        fields = [
            'vessel_name',
            'vessel_loa',
            'vessel_status'
        ]



 



