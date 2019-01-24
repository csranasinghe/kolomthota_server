from rest_framework import serializers

from shipping_line.models import Vessel, VesselArrival
from accounts.models import ShippingAgent, Account


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = ('id', 'vessel_status', 'vessel_loa', 'loa', 'vessel_name')


class VesselArrivalSerializer(serializers.ModelSerializer):

    class Meta:
        model = VesselArrival
        read_only_fields = ('shipping_line', )
        fields = (
            'id',
            'shipping_agent',
            'eta',
            'dis',
            'load',
            'ref_no',
            'draft_arrival',
            'draft_departure',
            'remarks',
            'service',
            'last_port',
            'next_port',
            'vessel',
            'vessel_name'
        )


class ShippingAgentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAgent
        fields = ('shipping_line', 'account')


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'user_type')