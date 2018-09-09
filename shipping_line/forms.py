from django.forms import ModelForm  
from .models import ShippingLine,VesselArrival


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



 



