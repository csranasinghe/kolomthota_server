from django.conf.urls import url, include
from .views import (
    vessel_listview,
    berth_schedule,
    view_history,
    remove_arrival,
    edit_arrival,
    vessel_timestamp,
    edit_arrival_done,
    vessel_info_details,
    remove_vessel,
    connot_remove_vessel,
    edit_vessel,
    edit_vessel_done

)

urlpatterns = [
    url('^$', vessel_listview, name="index"), 
    url('^vessel-details/$', vessel_info_details, name='vessel_info_details'),
    url('^vessel-timestamp/$', vessel_timestamp, name="vessel_timestamp"),
    url('^berth-schedule/$', berth_schedule, name="berthSchedule"),
    url('^history/$', view_history, name="viewHistory"),
    url('^remove_items/(?P<item_id>[0-9]+)/$', remove_arrival, name="remove_arrival"),
    url('^remove-vessel/(?P<item_id>[0-9]+)/$', remove_vessel, name="remove_vessel"),
    url('^delete-warning/', connot_remove_vessel, name="connot_remove_vessel"),
    url('^edit_vessels/(?P<item_id>[0-9]+)/$', edit_arrival, name="edit_arrival"),
    url('^edit-vessel/(?P<item_id>[0-9]+)/$', edit_vessel, name = 'edit_vessel'),
    url('^edit_vessels/(?P<item_id>[0-9]+)/edit/$', edit_arrival_done, name="edit_arrival_done"),
    url('^edit-vessel/(?P<item_id>[0-9]+)/edit_vessel/$', edit_vessel_done, name="edit_vessel_done")
]
