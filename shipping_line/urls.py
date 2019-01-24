from django.conf.urls import url, include
from .views import (
    vessel_listview,
    berth_schedule,
    view_history,
    remove_arrival,
    edit_arrival,
    vessel_timestamp
)

urlpatterns = [
    url('^$', vessel_listview, name="index"), 
    url('^vessel-timestamp/$', vessel_timestamp, name="vessel_timestamp"),
    url('^berth-schedule/$', berth_schedule, name="berthSchedule"),
    url('^history/$', view_history, name="viewHistory"),
    url('^remove_items/(?P<item_id>[0-9]+)/$', remove_arrival, name="remove_arrival"),
    url('^edit_vessels/(?P<item_id>[0-9]+)/$', edit_arrival, name="edit_arrival")
]
