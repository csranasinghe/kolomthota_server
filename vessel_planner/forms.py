from django.forms import ModelForm  
from shipping_line.models import VesselArrival
from .models import Messages , VesselProgress

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

class MessageSend(ModelForm):
    class Meta:
        model = Messages
        fields = [
            'message_author',
            'message'
        ]

class VesselProgressForm(ModelForm):
    class Meta:
        model = VesselProgress
        fields = [
           'vessel',
            'dis',
            'load'  
        ]