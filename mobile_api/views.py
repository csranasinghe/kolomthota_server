from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from shipping_line.models import Vessel, VesselArrival
from .serializers import VesselSerializer, VesselArrivalSerializer
from rest_framework import status
from rest_framework.response import Response

class VesselViewSet(ModelViewSet):
    """
    A model viewset for viewing and editing Vessel instances.
    """
    serializer_class = VesselSerializer
    queryset = Vessel.objects.all()


class VesselArrivalViewSet(ModelViewSet):
    """
    A model viewset for viewing and editing Vessel Arrival instances.
    """
    serializer_class = VesselArrivalSerializer
    queryset = VesselArrival.objects.all()



class ShippingAgentRegister(APIView):
    """
    A model viewset for viewing and editing Vessel Arrival instances.
    """

    def post(self, request, format=None):
        return Response({'msg': 'Successfully registered.'})