import datetime

from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from berth_planner.models import Berth
from shipping_line.models import Vessel, VesselArrival
from accounts.models import ShippingAgent, Account
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
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
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        a = self.request.user
        queryset = VesselArrival.objects.filter(shipping_agent__shipping_line=a.sa_account.shipping_line)

        return queryset


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
            'shipping_line': request.data.get('shipping_line', None),
            'account': account.id})
        sa_serializer.is_valid(raise_exception=True)
        sh_agent = sa_serializer.save()

        return Response({"msg": "Shipping line agent account created successfully."}, status=status.HTTP_201_CREATED)


class ShippingAgentDetails(APIView):
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        a = request.user
        sh_agent = get_object_or_404(ShippingAgent, account__id=a.id)
        return Response({
            'id': a.id,
            'email': a.email,
            'first_name': a.first_name,
            'last_name': a.last_name,
            'shipping_line': sh_agent.shipping_line.id,
            'shipping_line_name': sh_agent.shipping_line.name,
        })


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


class PublishedScheduleAPIView(APIView):
    """
    API view to get the published schedule
    """
    def get(self, request):
        return Response({'from': "2019-01-29", 'to': "2019-01-31", 'schedule': [
            {
                "id": 9,
                "eta": "2019-01-30T14:30:46Z",
                "etb": "2019-01-30T15:30:46Z",
                "etc": "2019-01-31T15:30:46Z",
                "berth_no": "1MN",
                "dis": 200,
                "load": 700,
                "ref_no": "MOEI905AJ",
                "remarks": "MSC,TO SHIFFTED TO 1MS ARR:1700-29/01",
                "service": "CC",
                "vessel_status": "M",
                "vessel_loa": "150",
                "vessel_name": "msa1",

            }, {
                "id": 10,
                "eta": "2019-01-31T15:30:46Z",
                "etb": "2019-01-31T17:30:46Z",
                "etc": "2019-02-01T15:30:46Z",
                "berth_no": "UCT2",
                "dis": 1002,
                "load": 0,
                "ref_no": "MSLV901RJ",
                "remarks": "13 ACROSS DFT 8.9M",
                "service": "IMED",
                "vessel_status": "F",
                "vessel_loa": "241",
                "vessel_name": "MSC LEVINA",

            },
        ]})


class UpcomingVesselArrivals(ListAPIView):
    serializer_class = UpcomingVesselArrivalsSerializer
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        a = self.request.user
        queryset = VesselArrival.objects.filter(shipping_agent__shipping_line=a.sa_account.shipping_line,
                                                eta__gte=datetime.datetime.now())

        return queryset


class Logout(APIView):
    """
    A view for handle logout functionality
    TODO: add token to a blacklisted token model
    """

    def get(self, request):
        return Response({'msg': 'Successfully logged out.'})


class BerthsList(ListAPIView):
    queryset = Berth.objects.all()
    serializer_class = BerthSerializer
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )


class BerthScheduleAPIView(APIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        vessel_arrival = get_object_or_404(VesselArrival, id=request.data.get('id', -1))
        vessel_arrival.is_scheduled = True
        vessel_arrival.schedule_details = {'group': request.data.get('group'),
                                           'start': request.data.get('start'),
                                           'end': request.data.get('end')}
        vessel_arrival.save()
        return Response({'msg': 'Added to the schedule.'})

    def get(self, request):
        # Vessel arrivals which are added to the schedule and not removed by user
        vessel_arrivals = VesselArrival.objects.filter(is_rejected_user=False, is_scheduled=True)
        resp = []
        for va in vessel_arrivals:
            resp.append({'schedule_details': va.schedule_details, 'vessel_name': va.vessel.vessel_name,
                         'total': va.total, 'vessel_loa': va.vessel.vessel_loa, 'eta': va.eta, 'service': va.service,
                         'remarks': va.remarks, 'id': va.id
                         })

        return Response(resp)


class BerthScheduleDeleteEditAPIView(APIView):

    def get(self, request, va_id):
        vessel_arrival = get_object_or_404(VesselArrival, id=va_id)
        vessel_arrival.is_scheduled = False
        vessel_arrival.schedule_details = {}
        vessel_arrival.save()
        return Response({'msg': 'Removed from schedule successfully.'})

    def post(self, request, va_id):
        vessel_arrival = get_object_or_404(VesselArrival, id=va_id)
        vessel_arrival.is_scheduled = True
        vessel_arrival.schedule_details = {'group': request.data.get('group'),
                                           'start': request.data.get('start'),
                                           'end': request.data.get('end')}
        vessel_arrival.save()
        return Response({'msg': 'Updated the schedule.'})