from django.conf.urls import url, include
from .views import index,addVessel,add_vessel_details,vessel_listview

urlpatterns = [
    url('^$', vessel_listview, name="index"),
    url('^vessel-details/$', add_vessel_details, name="addVessel"),  
]
