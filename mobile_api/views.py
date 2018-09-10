from rest_framework.viewsets import ModelViewSet
from shipping_line.models import Vessel, VesselArrival
from .serializers import VesselSerializer, VesselArrivalSerializer


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
