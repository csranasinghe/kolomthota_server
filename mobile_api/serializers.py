from rest_framework import serializers

from shipping_line.models import Vessel, VesselArrival, ShippingLine
from berth_planner.models import Berth
from accounts.models import ShippingAgent, Account


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = ('id', 'vessel_status', 'vessel_loa', 'loa', 'vessel_name')


class VesselArrivalSerializer(serializers.ModelSerializer):

    class Meta:
        model = VesselArrival
        read_only_fields = ('shipping_line', 'is_reviewed', 'is_rejected_user', 'is_rejected_BP',
                            'first_confirm', 'second_confirm', 'third_confirm')
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
            'vessel_name',
            'is_reviewed',
            'is_rejected_user',
            'is_rejected_BP',
            'first_confirm',
            'second_confirm',
            'third_confirm'
        )


class UpcomingVesselArrivalsSerializer(serializers.ModelSerializer):

    class Meta:
        model = VesselArrival
        fields = (
            'id',
            'eta',
            'vessel',
            'vessel_name',
            'is_reviewed',
            'is_rejected_user',
            'is_rejected_BP',
            'first_confirm',
            'second_confirm',
            'third_confirm'
        )


class ShippingAgentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAgent
        fields = ('shipping_line', 'account')


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'user_type')


class ShippingLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingLine
        fields = ('id', 'name', 'email')


class BerthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berth
        fields = ['id', 'name', 'max_length', 'max_across', 'max_draft', 'order']