from django.forms import ModelForm  
from .models import ShippingLine,VesselDetails

class VesselDetailsForm(ModelForm):
    class Meta:
        model = VesselDetails
        fields = [
            'vessel_name',
            'shipping_agent',
            'eta',
            'dis',
            'load',
            'total',
            'loa_val',
            'vessel_status',
            'ref_no',
            'draft_arrival',
            'draft_departure',
            'remarks',
            'service'
        ]



 



