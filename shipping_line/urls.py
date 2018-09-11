from django.conf.urls import url, include
from .views import vessel_listview,berth_schedule,view_history

urlpatterns = [
    url('^$', vessel_listview, name="index"), 
    url('^berth-schedule/$', berth_schedule, name="berthSchedule"),
    url('^history/$', view_history, name="viewHistory"),
]
