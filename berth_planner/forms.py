from django.forms import ModelForm  
from shipping_line.models import VesselArrival
from vessel_planner.models import Messages

class MessagesChecking(ModelForm):
    # eta = DateTimeField(input_formats=['%d/%m/%Y %H:%M:%S'], widget=DateTimeInput(format='%d/%m/%Y %H:%M:%S'))
    class Meta:
        model = Messages
        fields = [
            'is_reviewed'
        ]
