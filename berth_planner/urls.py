from django.conf.urls import url, include
from .views import index, schedule_published, vessel_arrivals, vessel_arrivals_review 

urlpatterns = [
    url('^$', index, name="index"),
    url('^schedule/published$', schedule_published, name="schedule_published"),
    url('^vessel-arrivals$', vessel_arrivals, name="vessel_arrivals"),
    url('^vessel-arrivals/(?P<id>\d+)/(?P<review_status>[-\w]+)$', vessel_arrivals_review, name="vessel_arrivals_review"),

]
