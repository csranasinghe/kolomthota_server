from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from shipping_line.models import Vessel, VesselArrival
from accounts.models import ShippingAgent, Account
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


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
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class ShippingAgentAPIView(APIView):
    """
    API view to register new shipping line agents and update existing shipping line agents.
    TODO: Add put and get methods
    """
    def post(self, request):
        account_serializer = UserAccountSerializer(data=request.data)
        account_serializer.is_valid(raise_exception=True)
        account = account_serializer.save()

        sa_serializer = ShippingAgentAccountSerializer(data={
            'shipping_line': request.data.get('shipping_line_id', None),
            'account': account.id})
        sa_serializer.is_valid(raise_exception=True)
        sh_agent = sa_serializer.save()

        return Response({"msg": "Shipping line agent account created successfully."}, status=status.HTTP_201_CREATED)


class ShippingLinesListAPIView(ListAPIView):
    """
    API view to retrieve the list of registered shipping lines.
    """
    serializer_class = ShippingLineSerializer
    queryset = ShippingLine.objects.all()


class Logout(APIView):
    """
    A view for handle logout functionality
    TODO: add token to a blacklisted token model
    """

    def get(self, request, format=None):
        return Response({'msg': 'Successfully logged out.'})

