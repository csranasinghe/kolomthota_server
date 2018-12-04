from django.conf.urls import url, include
from .views import vessel_listview,berth_schedule,view_history,remove_arrival,edit_arrival

urlpatterns = [
    url('^$', vessel_listview, name="index"), 
    url('^berth-schedule/$', berth_schedule, name="berthSchedule"),
    url('^history/$', view_history, name="viewHistory"),
    url('^remove_items/(?P<item_id>[0-9]+)/$', remove_arrival, name="remove_arrival"),
    url('^edit_vessels/(?P<item_id>[0-9]+)/$', edit_arrival, name="edit_arrival")
]
