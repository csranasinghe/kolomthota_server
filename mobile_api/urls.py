from .views import VesselViewSet, VesselArrivalViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = DefaultRouter()
router.register(r'vessels', VesselViewSet, base_name='vessel')
router.register(r'vessel-arrivals', VesselArrivalViewSet, base_name='vessel_arrival')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/token', obtain_jwt_token),
    url(r'^auth/token/refresh', refresh_jwt_token),
]