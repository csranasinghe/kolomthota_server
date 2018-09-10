from django.conf.urls import url, include
from .views import add_vessel_details,vessel_listview,berth_schedule,view_history

urlpatterns = [
    url('^$', vessel_listview, name="index"),
    url('^vessel-details/$', add_vessel_details, name="addVessel"), 
    url('^berth-schedule/$', berth_schedule, name="berthSchedule"),
    url('^history/$', view_history, name="viewHistory"),
]
