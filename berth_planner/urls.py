from django.conf.urls import url, include
from .views import index, schedule_published, vessel_arrivals, vessel_arrivals_review , show_messages , mark_as_read ,mark_as_unread
urlpatterns = [
    url('^$', index, name="index"),
    url('^messages$',show_messages , name="show_messages"),
    url('^schedule/published$', schedule_published, name="schedule_published"),
    url('^vessel-arrivals$', vessel_arrivals, name="vessel_arrivals"),
    url('^vessel-arrivals/(?P<id>\d+)/(?P<review_status>[-\w]+)$', vessel_arrivals_review, name="vessel_arrivals_review"),
    url('^edit_message/(?P<item_id>[0-9]+)/$', mark_as_read, name="mark_as_read"),
    url('^re_edit_message/(?P<item_id>[0-9]+)/$', mark_as_unread, name="mark_as_unread"),
]
