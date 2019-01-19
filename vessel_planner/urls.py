from django.conf.urls import url, include
from .views import vessel_dashboard ,progress , remove_vessel_progress

urlpatterns = [
    url('^$', vessel_dashboard, name="index"),
    url('^edit_details/(?P<item_id>[0-9]+)/$', progress, name="progress"),
    url('^delete_details/(?P<item_id>[0-9]+)/$', remove_vessel_progress, name="remove_progress"),
]