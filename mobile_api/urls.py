from .views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = DefaultRouter()
router.register(r'vessels', VesselViewSet, base_name='vessel')
router.register(r'vessel-arrivals', VesselArrivalViewSet, base_name='vessel_arrival')
router.register

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/token$', obtain_jwt_token),
    url(r'^auth/token/refresh$', refresh_jwt_token),
    url(r'^logout$', Logout.as_view()),
    url(r'^users/sa$', ShippingAgentAPIView.as_view()),
    url(r'^users/sa/me$', ShippingAgentDetails.as_view()),
    url(r'^users/sa/(?P<username_hash>[\w.@+-]+)$', CheckUsernameAPIView.as_view()),
    url(r'^shipping-lines$', ShippingLinesListAPIView.as_view()),
    url(r'^published-schedule$', PublishedScheduleAPIView.as_view()),
    url(r'^varrivals/upcoming$', UpcomingVesselArrivals.as_view()),

    # Web API endpoints
    url(r'^berths$', BerthsList.as_view()),
    url(r'^berth-schedule$', BerthScheduleAPIView.as_view()),


]