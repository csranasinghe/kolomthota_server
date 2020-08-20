from django.forms import ModelForm ,  DateTimeField, DateTimeInput
from .models import ShippingLine, VesselArrival,Vessel


class VesselArrivalDetailsForm(ModelForm):
    # eta = DateTimeField(input_formats=['%d/%m/%Y %H:%M:%S'], widget=DateTimeInput(format='%d/%m/%Y %H:%M:%S'))
    class Meta:
        model = VesselArrival
        exclude = [
            'first_confirm',
            'second_confirm',
            'third_confirm',
            'modified_time',
            'created_time',

        ]

class VesselDetailsForm(ModelForm):
    class Meta:
        model = Vessel
        fields = [
            'vessel_name',
            'vessel_loa',
            'vessel_status',
            'author'
        ]



 



