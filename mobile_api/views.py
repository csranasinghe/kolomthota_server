from django.shortcuts import get_object_or_404

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


class CheckUsernameAPIView(APIView):
    """
    API view to check for username availability
    TODO: get the encrypted username and decrypt it using a secret which is known by trusted apps
    """
    def get(self, request, username_hash=None):
        if username_hash:
            account = get_object_or_404(Account, username=username_hash)
            if account:
                return Response({'msg': 'The username already exists.'})
        return Response({'msg': "Bad request."}, status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    """
    A view for handle logout functionality
    TODO: add token to a blacklisted token model
    """

    def get(self, request):
        return Response({'msg': 'Successfully logged out.'})

