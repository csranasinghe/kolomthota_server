from .views import VesselViewSet, VesselArrivalViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'vessels', VesselViewSet, base_name='vessel')
router.register(r'vessel-arrivals', VesselArrivalViewSet, base_name='vessel_arrival')
urlpatterns = router.urls
